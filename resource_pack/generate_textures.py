from PIL import Image, ImageDraw
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "textures" / "blocks"
OUT.mkdir(parents=True, exist_ok=True)

colors = {
    "water_lime": (110, 255, 80, 180),
    "water_cyan": (80, 220, 255, 180),
    "water_red": (255, 80, 80, 180),
    "water_orange": (255, 170, 70, 180),
    "water_purple": (180, 95, 255, 180),
    "water_lightblue": (130, 210, 255, 180),
    "water_darkblue": (42, 82, 190, 180),
    "water_indigo": (90, 90, 220, 180),
    "water_aqua": (90, 255, 240, 180),
    "water_yellow": (255, 234, 80, 180),
}

for name, rgba in colors.items():
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 16, 16), fill=rgba)
    for y in range(16):
        alpha = int(120 + (y / 15) * 60)
        color = (rgba[0], rgba[1], rgba[2], alpha)
        draw.line((0, y, 15, y), fill=color, width=1)
    for i in range(30):
        x = (i * 13) % 16
        y = (i * 7) % 16
        draw.point((x, y), fill=(255, 255, 255, 40))
    img.save(OUT / f"{name}.png")

print("Texturas generadas:", ", ".join(sorted(colors.keys())))
