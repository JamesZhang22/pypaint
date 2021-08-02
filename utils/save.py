import png
from typing import List

def save(image: List) -> None:
     convert = []
     for row in image:
          tuple_row = []
          for color in row:
               for rgb_value in color:
                    tuple_row.append(rgb_value)
          convert.append(tuple(tuple_row))

     dimensions = len(image)
     f = open('drawings/pypaint.png', 'wb')
     w = png.Writer(dimensions, dimensions, greyscale=False)
     w.write(f, convert)
     f.close()

     
