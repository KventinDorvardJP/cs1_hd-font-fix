# Trails of Cold Steel I — Russian HD Font Spacing Fix

Fixes excessively spaced Cyrillic text when **High Resolution Font** is enabled in the PC version of *The Legend of Heroes: Trails of Cold Steel* with the Russian fan translation.

**Verified in-game.** The original HD font renders Russian dialogue with gaps between letters (`Э т о  ж е...`); the patched font corrects the spacing.

## Installation

1. Back up `data/fonts/font_ru_hd.itf` in your game directory.
2. Place the original `font_ru_hd.itf` alongside `patch_cs1_ru_hd.py`.
3. Run `python patch_cs1_ru_hd.py` (Python 3 required).
4. Rename the generated `font_ru_hd_experimental.itf` to `font_ru_hd.itf` and copy it into `data/fonts`, replacing the original.
5. Enable **High Resolution Font** in the game's configuration tool.

To revert, restore your backed-up `font_ru_hd.itf`.

## Alternate installatiow way

1. Download already pathed `patch_cs1_ru_hd.itf` from this reposetory.
2. Place the downloaded `patch_cs1_ru_hd.itf` alongside `data/fonts/font_ru_hd.itf` in the game directory.
3. Back up original `data/fonts/font_ru_hd.itf` in your game directory.
4. Rename the downloaded `cs1_russian_hd_font_fix.itf` to `font_ru_hd.itf`.
5. Enable **High Resolution Font** in the game's configuration tool.

To revert, restore your backed-up `font_ru_hd.itf`.

## How it works

The patch adjusts horizontal offsets and advance widths for selected Cyrillic characters and punctuation in the HD `.itf` font. It leaves glyph artwork and translation text unchanged.

## Credits

Created with assistance from ChatGPT, informed by [FalcomFontCreator](https://github.com/TwnKey/FalcomFontCreator)'s ITF format research.
