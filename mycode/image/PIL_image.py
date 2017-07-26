from PIL import Image
im = Image.open("D:\mycode\image\\timg.png")
print(im.format,im.size,im.mode)
print(im.show())