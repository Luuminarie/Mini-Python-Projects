import qrcode

link = input("Enter the URL for which you want to generate a QR code: ")

img = qrcode.make(link)
type(img)  # qrcode.image.pil.PilImage
img.save('example_qrcode.png')