from captcha.image import ImageCaptcha
import os
import urllib.request
from PIL import Image, ImageOps

intext = open("indat.txt","r").read().upper()

fls = []
ln_num = 0
for ln in intext.split("\n"):
  if len(ln) <= 2:
    pass
  else:
    ln_num += 1
    image = ImageCaptcha(fonts={"f1.ttf"}, width=1500, height =150)
    data = image.generate(ln)
    ofile = f"o{ln_num}.png"
    fls.append(ofile)
    image.write(ln, ofile)

img1 = Image.open("bd.png")
dn = 0
for i1 in fls:
  dn += 150
  IM = Image.open(i1)
  img1.paste(IM, (0,dn)) 

img2 = img1.convert("L")
im_invert = ImageOps.invert(img2)
im_invert.save('out.png', quality=95)
