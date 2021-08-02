from PIL import Image
from typing import List

def load(file_name: str) -> List:
    path = "drawings/" + file_name 
    img = Image.open(path)
    w, h = img.size
    rgb = list(img.getdata())
    new = []
    row = []
    for i in range(len(rgb)):
        if i % w == 0:
            new.append(row)
            row = []
            row.append(rgb[i])
        else:
            row.append(rgb[i])
    new.append(row)

    return h, new[1:]