# 🖼️ Random Wallpaper

<p align="center">
  <strong>Random wallpaper rotation every 5 minutes</strong>
</p>

<!-- WALLPAPER_START -->
<img src="./randomizer/wallpapers/wallpaper01.jpg" width="100%" alt="Random wallpaper" />
<!-- WALLPAPER_END -->

## ✨ How it works

GitHub Actions randomly selects one of the JPG/JPEG wallpapers in `randomizer/wallpapers/` and updates the image above every **5 minutes**.

## 📁 Structure

```text
.
├── .github/
│   └── workflows/
│       └── wallpaper.yml
├── randomizer/
│   └── wallpapers/
│       ├── wallpaper01.jpg
│       ├── wallpaper02.jpg
│       ├── ...
│       └── wallpaper10.jpg
└── README.md
```

## ⏱️ Schedule

```yaml
cron: "*/5 * * * *"
```

GitHub attempts to run the workflow every 5 minutes. Scheduled Actions can occasionally be delayed by GitHub during high-load periods.

## ⚙️ Important GitHub setting

The workflow uses:

```yaml
permissions:
  contents: write
```

If the workflow cannot push the README update, open:

**Settings → Actions → General → Workflow permissions**

and enable **Read and write permissions**.

## 🖼️ Wallpapers

Put your `.jpg` or `.jpeg` files inside:

```text
randomizer/wallpapers/
```

The workflow automatically detects them, so you can have 10 or more wallpapers.

## 👤 GitHub

https://github.com/initchirag

> This project changes the image displayed in the GitHub README. It does not change your Windows desktop wallpaper.
