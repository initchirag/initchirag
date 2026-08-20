# 🖼️ Wallpaper Randomizer

A lightweight Windows wallpaper changer that randomly rotates wallpapers every **20 minutes**.

## Features

- Supports 20+ wallpapers
- Randomly shuffles wallpapers
- Changes wallpaper every 20 minutes
- Avoids immediately repeating the same wallpaper
- No external Python packages required

## Project Structure

```text
wallpaper-randomizer/
├── main.py
├── README.md
└── wallpapers/
    └── Put your wallpapers here
```

## Requirements

- Windows
- Python 3.x

## Run

```bash
python main.py
```

The program will continuously change your desktop wallpaper every 20 minutes.

## Add Wallpapers

Put `.jpg`, `.jpeg`, `.png`, `.bmp`, or `.webp` images inside the `wallpapers` folder.

## Change the Interval

In `main.py`:

```python
INTERVAL = 20 * 60
```

For example, 10 minutes:

```python
INTERVAL = 10 * 60
```
