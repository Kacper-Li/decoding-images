from PIL import Image
from pprint import pprint

if __name__ == "__main__":

    clr_trans = {
        (232, 3, 138, 255) : "⬜️",
        (58, 185, 229, 255) : "🟩"
    }

    img = Image.open("puzzle.png")
    print(img.mode)
    print(img.size)
    print(img.getcolors())
    print("----------------")
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            pixel = img.getpixel((x,y))
            clr = clr_trans.get(pixel, "XXX")
            print(clr,end="")
        print("")