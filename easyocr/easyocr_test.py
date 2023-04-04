import easyocr
import os
import cv2
from glob import glob

image_paths = glob("../data/*.jpeg")
reader = easyocr.Reader(["en"])
for image_path in image_paths:
    image = cv2.imread(image_path)
    result = reader.readtext(image)
    fulltext = ""
    for (coord, text, prob) in result:
        (topleft, topright, bottomright, bottomleft) = coord
        tx, ty = (int(topleft[0]), int(topleft[1]))
        bx, by = (int(bottomright[0]), int(bottomright[1]))
        image = cv2.rectangle(image, (tx, ty), (bx, by), (0, 0, 255), 5)
        fulltext += text.strip()
    if len(result) != 0:
        cv2.imwrite("en"+os.path.basename(image_path), image)
        print("\t".join([fulltext, os.path.basename(image_path)]))
