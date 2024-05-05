
import qrcode


# 1. simple QR generator

# img = qrcode.make("Hello, I am Engineering Undergraduate student")
# img.save("mycode.png")


#  2. Advance option for creating QR code

'''
qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_L,
                   box_size = 20,
                   border = 2)

qr.add_data("https://www.mygreatlearning.com/academy#explore_courses")
qr.make(fit = True)

img= qr.make_image(fill_color="black",back_color="white")
img.save("advanced.png")

'''

#  3. create SVG images

import qrcode.image.svg

factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make("Hello World! ", image_factory = factory)
svg_img.save("MYQRCODE.svg")