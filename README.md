# Seventeen Syllables of Debugging

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![Python](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Entry for the make.fun bounty
[Seventeen Syllables of Debugging](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605).

## The haiku

```text
breakpoint holds its breath
one wrong line, the whole night bends
semicolon, gone
```

Three lines, 5-7-5 syllables, 81 characters.

## How it works

`main.py` (Python 3.13, standard library only) writes the haiku above to
`/output/entry.txt` — exactly 81 bytes, no trailing newline, byte-identical
on every run.

```bash
python3 main.py
cat /output/entry.txt
```
