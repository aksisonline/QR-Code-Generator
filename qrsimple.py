import qrcode
s = input()
img = qrcode.make(s)
img.save("./Generated/" + "red" + ".png")