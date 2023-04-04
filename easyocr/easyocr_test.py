import easyocr
import os
from PIL import Image, ImageDraw, ImageFont
from glob import glob


def puttext(img, text, box, color=(255, 0, 0)):
    size = int(min(img.size) / 20)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(
        font=r"/System/Library/Fonts/Hiragino Sans GB.ttc", size=size
    )
    tx, ty, bx, by = box
    draw.text(xy=(tx, ty - (size + 5)), text=text, fill=(255, 0, 0), font=font)
    if tx < bx and ty < by:
        draw.rectangle(xy=(tx, ty, bx, by), outline=color, width=int(size / 10))
    return image


image_paths = glob("../data/*.jpeg")
reader = easyocr.Reader(["ja", "en"])
for image_path in image_paths:
    image = Image.open(image_path)
    result = reader.readtext(image)

    if len(result) != 0:
        for (coord, text, prob) in result:
            (topleft, topright, bottomright, bottomleft) = coord
            tx, ty = (int(topleft[0]), int(topleft[1]))
            bx, by = (int(bottomright[0]), int(bottomright[1]))
            image = puttext(image, text, (tx, ty, bx, by))
        image.save(os.path.basename(image_path))
