Add-Type @"
using System;
using System.Runtime.InteropServices;

public class Wallpaper {
    [DllImport("user32.dll", CharSet = CharSet.Unicode)]
    public static extern bool SystemParametersInfo(
        uint uiAction,
        uint uiParam,
        string pvParam,
        uint fWinIni
    );
}
"@

$wallpaperFolder = Join-Path $PSScriptRoot "wallpapers"

if (-not (Test-Path $wallpaperFolder)) {
    Write-Host "ERROR: wallpapers folder not found!"
    Write-Host "Expected: $wallpaperFolder"
    exit 1
}

# Get JPG/JPEG wallpapers
$wallpapers = @(
    Get-ChildItem -Path $wallpaperFolder -File |
    Where-Object {
        $_.Extension -match '^\.(jpg|jpeg)$'
    }
)

if ($wallpapers.Count -eq 0) {
    Write-Host "ERROR: No JPG wallpapers found!"
    Write-Host "Put your JPG files inside the wallpapers folder."
    exit 1
}

Write-Host "=========================================="
Write-Host "       RANDOM WALLPAPER CHANGER"
Write-Host "=========================================="
Write-Host ""
Write-Host "Found $($wallpapers.Count) wallpapers."
Write-Host "Changing wallpaper every 5 minutes."
Write-Host "Press CTRL+C to stop."
Write-Host ""

$previousWallpaper = $null

while ($true) {

    $availableWallpapers = @(
        $wallpapers | Where-Object {
            $_.FullName -ne $previousWallpaper
        }
    )

    $randomWallpaper = Get-Random -InputObject $availableWallpapers

    Write-Host "Changing wallpaper to: $($randomWallpaper.Name)"

    $success = [Wallpaper]::SystemParametersInfo(
        20,
        0,
        $randomWallpaper.FullName,
        3
    )

    if ($success) {
        Write-Host "Wallpaper changed successfully."
    }
    else {
        Write-Host "ERROR: Windows could not change the wallpaper."
    }

    Write-Host "Next wallpaper in 5 minutes..."
    Write-Host ""

    $previousWallpaper = $randomWallpaper.FullName
    
    Start-Sleep -Seconds 300
}
