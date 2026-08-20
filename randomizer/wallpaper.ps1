# Wallpaper Randomizer
# Changes to a random wallpaper every 20 minutes

Add-Type @"
using System;
using System.Runtime.InteropServices;

public class Wallpaper {
    [DllImport("user32.dll", CharSet = CharSet.Auto)]
    public static extern int SystemParametersInfo(
        int uAction,
        int uParam,
        string lpvParam,
        int fuWinIni
    );
}
"@

$wallpaperFolder = Join-Path $PSScriptRoot "wallpapers"

$wallpapers = Get-ChildItem -Path $wallpaperFolder -Filter "*.png"

if ($wallpapers.Count -eq 0) {
    Write-Host "No PNG wallpapers found in the wallpapers folder."
    exit
}

while ($true) {

    # Select a random wallpaper
    $randomWallpaper = Get-Random -InputObject $wallpapers

    Write-Host "Changing wallpaper to: $($randomWallpaper.Name)"

    # Set wallpaper
    [Wallpaper]::SystemParametersInfo(
        20,
        0,
        $randomWallpaper.FullName,
        3
    )

    # Wait 20 minutes
    Start-Sleep -Seconds 1200
}