# Scary Drama / Film Terminal Text Looper

A lightweight prop script for film and drama scenes that displays a continuous, frantic distress loop in a visible terminal.

## Scene Context
Designed for horror, sci-fi, psychological thriller, or supernatural drama productions where a computer terminal, hacker monitor, or distress screen displays uncontrollable looping distress messages.

### Message Content
> *"I WANT TO GO HOME, I WANT TO GO HOME, I WANT TO GO HOME !!! I DON’T WANT TO BE WITH THE ALIEN !!! I DON’T WANT TO BE WITH THE SPIRIT !!! I HATE THE ALIENS AND SPIRITS SO DEEP MORE THAN BOTTOMLESS PIT !!! ... I WANT TO GO HOME !!! ... "*

The complete script contains the full 15,769-character extended distress monologue (4,168 words / 406 phrases), preserved in `text.txt` and embedded in `loop.py`.

## Quick Start

### 1. Direct Python Execution
```bash
python loop.py
```

### 2. Windows 1-Click Launchers
- **`start.bat`**: Double-click to launch in Command Prompt with black background and red text.
- **`start.ps1`**: PowerShell script with configurable arguments.

## Customization Options

```bash
python loop.py --help
```

| Flag | Options | Default | Description |
|---|---|---|---|
| `--mode` | `words`, `lines`, `block` | `words` | Streaming mode: `words` streams word-by-word; `lines` outputs phrase-by-phrase; `block` prints the full text block. |
| `--delay` | Float (e.g. `0.02`, `0.1`) | `0.03` | Delay between prints in seconds. Lower numbers produce frantic high-speed scrolling. |
| `--color` | `bold_red`, `red`, `green`, `yellow`, `cyan`, `white`, `none` | `bold_red` | ANSI terminal text color. |
| `--file` | File path | `text.txt` | Path to custom text file to loop on screen. |

### Production / Filming Examples

- **Frantic Alien Possessed Typing (Fast words)**:
  ```bash
  python loop.py --mode words --delay 0.015 --color bold_red
  ```

- **Retro Sci-Fi Green Matrix Stream**:
  ```bash
  python loop.py --mode lines --delay 0.05 --color green
  ```

- **Relentless Scrolling Horror Wall**:
  ```bash
  python loop.py --mode lines --delay 0.02 --color bold_red
  ```

## Production Tips for On-Camera Shooting
1. **Full-Screen Terminal**: Press `F11` (in Windows Terminal) or `Alt + Enter` (in Command Prompt) to make the terminal full screen.
2. **Font Size**: Zoom in with `Ctrl + MouseWheel` or terminal settings so text is clearly legible to cameras.
3. **Stopping**: Press `Ctrl + C` at any time to gracefully stop the loop between takes.
4. **Customizing Words On-Set**: Simply edit `text.txt` directly—no code modification needed.
