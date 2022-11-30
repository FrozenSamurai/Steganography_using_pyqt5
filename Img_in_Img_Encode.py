
from PIL import Image
''' from Img_in_Img_Main import * '''

MAX_COLOR_VALUE = 256
MAX_BIT_VALUE = 8
n_bits = 2
encoded_image_path = "C:\Steganography\Encoded.png"


class encimgclass():

    def make_image(data, resolution):
        image = Image.new("RGB", resolution)
        image.putdata(data)

        return image

    def remove_n_least_significant_bits(value, n):
        value = value >> n
        return value << n

    def get_n_most_significant_bits(value, n):
        return value >> MAX_BIT_VALUE - n

    def encode(self, e5, e6):
        print(e5, e6)

        image_to_hide = Image.open(e5, 'r')
        image_to_hide_in = Image.open(e6, 'r')

        width, height = image_to_hide.size
        hide_image = image_to_hide.load()
        hide_in_image = image_to_hide_in.load()

        data = []

        for y in range(height):
            for x in range(width):

                (r_hide, g_hide, b_hide, alpha) = hide_image[x, y]

                # (107, 3, 10)
                # most sig bits

                r_hide = encimgclass.get_n_most_significant_bits(
                    r_hide, n_bits)
                g_hide = encimgclass.get_n_most_significant_bits(
                    g_hide, n_bits)
                b_hide = encimgclass.get_n_most_significant_bits(
                    b_hide, n_bits)

                # remove lest n sig bits

                (r_hide_in, g_hide_in, b_hide_in, alpha) = hide_in_image[x, y]

                r_hide_in = encimgclass.remove_n_least_significant_bits(
                    r_hide_in, n_bits)
                g_hide_in = encimgclass.remove_n_least_significant_bits(
                    g_hide_in, n_bits)
                b_hide_in = encimgclass.remove_n_least_significant_bits(
                    b_hide_in, n_bits)

                data.append((r_hide + r_hide_in,
                            g_hide + g_hide_in,
                            b_hide + b_hide_in))

        encimgclass.make_image(
            data, image_to_hide.size).save(encoded_image_path)
