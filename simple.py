from PIL import Image
from pprint import pprint

if __name__ == "__main__":

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
    print("----------------")
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            pixel = img.getpixel((x,y))
            clr = clr_trans.get(pixel, "XXX")
            binary = bin_trans.get(pixel, "ERROR")
            pixel_values.append(binary)
            print(clr,end="")
        print("")
