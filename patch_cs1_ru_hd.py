
from pathlib import Path
import struct

source = Path("font_ru_hd.itf")
data = bytearray(source.read_bytes())

assert data[:2] == b"\x01\x01"
assert struct.unpack_from("<H", data, 2)[0] == 64

count = struct.unpack_from("<I", data, 8)[0]
seen = set()

for i in range(count):
    code, pos = struct.unpack_from("<II", data, 0x40 + i * 8)

    if code in seen or not (0x40 + 8 * count <= pos <= len(data) - 12):
        continue
    seen.add(code)

    punctuation = code in {0xAB, 0xBB, 0x2013, 0x2014, 0x2026}
    compact = code in {ord(c) for c in ".,:;!"}

    if not (0x400 <= code <= 0x4FF or punctuation or compact):
        continue

    width = struct.unpack_from("<H", data, pos)[0]
    x = struct.unpack_from("<h", data, pos + 6)[0]
    adv = struct.unpack_from("<h", data, pos + 8)[0]

    if not (0 < width <= 100 and 0 < adv <= 100):
        raise ValueError(f"Unexpected metric for U+{code:04X}")

    if compact:
        new_x, new_adv = 2, width + 3
    else:
        new_x = max(0, (32 - width) // 2)
        new_adv = width + new_x + max(
            0, min(2, adv - width - x)
        )

    struct.pack_into("<hh", data, pos + 6, new_x, new_adv)

output = source.with_name("font_ru_hd_fixed.itf")
output.write_bytes(data)
print("Wrote", output)
