from PIL import Image, ImageDraw, ImageFont

import pytesseract as tess

img = Image.new(mode="RGB", size=(1000, 1000))
d1 = ImageDraw.Draw(img)

font = ImageFont.truetype("arial.ttf", 28, encoding="unic")

f = open('quine.py','r')
d1.text((65, 10), ''.join(f.readlines()), fill =(255, 0, 0), font=font)
f.close()

img.save("output.png")

print(tess.image_to_string(Image.open('output.png')))

