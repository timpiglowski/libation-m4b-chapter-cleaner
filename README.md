# libation-m4b-chapter-cleaner
[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/) [![status: hibernate](https://github.com/GIScience/badges/raw/master/status/hibernate.svg)](https://github.com/GIScience/badges#hibernate)

When using [rmcrackan's Libation](https://github.com/rmcrackan/Libation) to save Audible audiobooks, you may encounter a problem where the chapters are not recognized correctly in [Prologue](https://prologue.audio).

This issue occurs because of a mismatch between different types of chapters within the audiobook file, as explained [here](https://www.reddit.com/r/PrologueApp/comments/uvu9rn/missing_chapters/).

To resolve this problem, you can use a [simple fix](https://github.com/prologueapp/Prologue/wiki/Common-Issues#embedded-chapters-arent-working) recommended in the 'Common Issues' section of Prologue's GitHub project page. This fix involves remuxing the audiobook file using the following command: `ffmpeg -i <input file> -map 0:a -map 0:v -c copy <output file>`

That's exactly what my script does. After running the script, you'll be prompted to select the problematic audiobook file. The script will then apply the fix and save the corrected version alongside the original file. Once you import the fixed version into Prologue, the chapters should work as expected.

## Usage
```python
python3 libation-m4b-chapter-cleaner.py
```

## Dependencies
- tkinter
- ffmpeg in PATH

## Notes
Remuxing in ffmpeg will NOT retain sort-title and sort-album metadata. For more info, see [Prologue's wiki](https://github.com/prologueapp/Prologue/wiki/Metadata#ffmpeg).
