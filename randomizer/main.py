import os
import random
import time
import ctypes

WALLPAPER_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wallpapers")
INTERVAL = 20 * 60  # 20 minutes

def get_wallpapers():
    extensions = (".jpg", ".jpeg", ".png", ".bmp", ".webp")
    return [
        os.path.join(WALLPAPER_FOLDER, file)
        for file in os.listdir(WALLPAPER_FOLDER)
        if file.lower().endswith(extensions)
    ]

def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

def main():
    if not os.path.exists(WALLPAPER_FOLDER):
        print("Error: wallpapers folder not found.")
        return

    wallpapers = get_wallpapers()

    if not wallpapers:
        print("No wallpapers found in the wallpapers folder.")
        return

    print(f"Found {len(wallpapers)} wallpapers.")
    print("Wallpaper changer started. Changing every 20 minutes.")

    last_wallpaper = None

    while True:
        shuffled = wallpapers.copy()
        random.shuffle(shuffled)

        for wallpaper in shuffled:
            if wallpaper == last_wallpaper and len(shuffled) > 1:
                continue

            set_wallpaper(wallpaper)
            print(f"Changed wallpaper to: {os.path.basename(wallpaper)}")
            last_wallpaper = wallpaper

            time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
