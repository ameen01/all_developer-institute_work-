from PIL import Image


def iamesize(image_name, image_size=(200, 200)):
    for image_name in image_name:
        img = Image.open(image_name)
        nimg = img.resize(image_size)
        Image.SAVE(nimg)


iame = ["LIK.JPG"]
iamesize(iame)