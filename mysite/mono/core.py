from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

fonts = {
    # First font is the default
    'fonts/monogram kk sc.ttf': 'Monogram KK',
    'fonts/antique_roman_swash.ttf': 'Antique Roman Swash',
}


class Core:

    def get_fonts(self):
        return fonts

    # renders and generates the image
    def render_image(initials, font):
        if not font:
            font = fonts[0]

        # font = 'fonts/monogram kk sc.ttf'
        print("font is " + font)
        font_size = 500  # font size defined (in px?)
        # dimensions of the panel
        width = font_size * 2
        height = font_size * 2
        y = 0  # zero variable used for lists
        z = (height / 2) - (font_size / 2)  # used for centering

        initials = initials.upper()
        chars = list(initials)
        image = Image.new('RGBA', (width, height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(font, font_size)
        sum = np.divide(
            np.subtract(width, np.add(np.add(font.getsize(chars[0]), font.getsize(chars[1])), font.getsize(chars[2]))),
            2)
        # This is black magic ^

        # get size of letters in each position
        one = sum
        two = np.add(one, font.getsize(chars[0]))
        three = np.add(sum, np.add(font.getsize(chars[0]), font.getsize(chars[1])))
        two_length = np.multiply(font.getsize(chars[1]), .3)
        one_cord = np.add(one, two_length)
        three_cord = np.subtract(three, two_length)

        # draw each letter in picture
        draw.text((one_cord[0], z), chars[y], fill=(0, 0, 0), font=font)
        draw.text((two[0], z), chars[y + 1], fill=(0, 0, 0), font=font)
        draw.text((three_cord[0], z), chars[y + 2], fill=(0, 0, 0), font=font)

        # text_height = font.getsize(l[0])
        draw.ellipse((font_size * 0.9, font_size * 0.1,
                      font_size * 1.1, font_size * 0.3
                      ), outline='green', width=10)
        draw.ellipse((0, 0, width, height), outline='red', width=10)
        # image.show()  # used for beguggin purposes
        file_path = "generated/" + initials + ".png"
        image.save("mono/" + file_path)
        return file_path

    # monogram = 'smp'  # input("Enter your initials in the order the you want the monogram to show: \n")
    # render_image(monogram)
    # output_image(monogram)
