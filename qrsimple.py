import qrcode
s = input()
img = qrcode.make(s)
img.save("./Generated/" + "qr_code" + ".png")