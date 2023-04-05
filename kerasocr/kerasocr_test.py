import keras_ocr 
import os
from PIL import Image, ImageDraw, ImageFont
from glob import glob
import matplotlib.pyplot as plt

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
    return img


image_paths = glob("../data/*.jpeg")
pipeline = keras_ocr.pipeline.Pipeline()

image = [keras_ocr.tools.read(image_path) for image_path in image_paths]
predict = pipeline.recognize(image)
fig, axs = plt.subplots(nrows=len(image), figsize=(10, 20))
for ax, img, predictions in zip(axs, image, predict):
    keras_ocr.tools.drawAnnotations(image=img, 
                                    predictions=predictions, 
                                    ax=ax)
    