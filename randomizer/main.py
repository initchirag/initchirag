import os
import random
import time
import ctypes

WALLPAPER_FOLDER = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "wallpapers"
)

CHANGE_EVERY = 5 * 60  

def get_wallpapers():
    supported_formats = (".jpg", ".jpeg", ".png", ".bmp")

    wallpapers = []

    for filename in os.listdir(WALLPAPER_FOLDER):
        if filename.lower().endswith(supported_formats):
            wallpapers.append(
                os.path.join(WALLPAPER_FOLDER, filename)
            )

    return wallpapers

def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(
        20,
        0,
        image_path,
        3
    )

def main():

    print("====================================")
    print("       RANDOM WALLPAPER CHANGER")
    print("====================================")

    if not os.path.exists(WALLPAPER_FOLDER):
        print("ERROR: wallpapers folder not found!")
        return

    wallpapers = get_wallpapers()

    if not wallpapers:
        print("ERROR: No wallpapers found!")
        return

    print(f"Found {len(wallpapers)} wallpapers.")
    print("Changing wallpaper every 5 minutes.")
    print("Press CTRL + C to stop.\n")

    last_wallpaper = None

    while True:

        available_wallpapers = [
            wallpaper
            for wallpaper in wallpapers
            if wallpaper != last_wallpaper
        ]

        wallpaper = random.choice(available_wallpapers)

        set_wallpaper(wallpaper)

        print(
            f"Changed to: {os.path.basename(wallpaper)}"
        )

        last_wallpaper = wallpaper

        print("Waiting 5 minutes...\n")
        time.sleep(5 * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nWallpaper changer stopped.")
