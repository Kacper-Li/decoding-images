from PIL import Image
from pprint import pprint
import logging

logging.basicConfig(
    filename='example.log',
    encoding='utf-8',
    level=logging.DEBUG,
    format='|%(asctime)s| %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p')

if __name__ == "__main__":

    logger = logging.getLogger(__name__)
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
    print(img.mode)
    print(img.size)
    print(img.getcolors())
    logger.info("Image of mode and size, %s %s, loaded.", img.mode, img.size)
    print("----------------")
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            pixel = img.getpixel((x,y))
            clr = clr_trans.get(pixel, "XXX")
            binary = bin_trans.get(pixel, "ERROR")
            pixel_values.append(binary)
            print(clr,end="")
    logger.info("Image read with %s rows %s columns", y,x)
    logger.info("Binary map of image created with %d values", len(pixel_values))
