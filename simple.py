from PIL import Image
from pprint import pprint
import logging

logging.basicConfig(
    filename='example.log',
    encoding='utf-8',
    level=logging.DEBUG,
    format='|%(asctime)s| %(message)s'
)

def count_consecutives(array: list) -> list:
    """Returns a Run length encoding of the arrays values. (how many consecutive numbers)"""
    count = 1
    consecutives = []
    value = array[0]
    for i, x in enumerate(array[1:]):
        if x == value:
            count += 1
        else:
            consecutives.append(count)
            value = x
            count = 1
    consecutives.append(count)
    return consecutives



if __name__ == "__main__":

    logger = logging.getLogger(__name__)
    logger.info("--------------------Starting-----------------------")
    clr_trans = {
        (232, 3, 138, 255) : "⬜️",
        (58, 185, 229, 255) : "🟩"
    }
    bin_trans = {
            (232, 3, 138, 255) : "0",
            (58, 185, 229, 255) : "1"
        }
    pixel_values = []
    img = Image.open("puzzle.png")
    logger.info("Image of mode and size, %s %s, loaded.", img.mode, img.size)
    logger.info("Colour makeup is %s", img.getcolors())
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            pixel = img.getpixel((x,y))
            clr = clr_trans.get(pixel, "XXX")
            binary = bin_trans.get(pixel, "ERROR")
            pixel_values.append(binary)
            print(clr,end="")
        print("")
    logger.info("Image read with %s rows %s columns", y,x)
    logger.info("Binary map of image created with %d values", len(pixel_values))
