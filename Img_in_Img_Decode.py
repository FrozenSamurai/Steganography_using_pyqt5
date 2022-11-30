
from PIL import Image


MAX_COLOR_VALUE = 256
MAX_BIT_VALUE = 8
n_bits = 2
decoded_image_path = "C:\Steganography\Decoded.png"


class dcdimgclass():
    def make_image(data, resolution):
        image = Image.new("RGB", resolution)
        image.putdata(data)
        image.show()

        return image

    def shit_n_bits_to_8(value, n):
        return value << MAX_BIT_VALUE - n

    def get_n_least_significant_bits(value, n):
        value = value << MAX_BIT_VALUE - n
        value = value % MAX_COLOR_VALUE
        return value >> MAX_BIT_VALUE - n

    def decode(self, e7):

        image_to_decode = Image.open(e7, 'r')

        width, height = image_to_decode.size
        encoded_image = image_to_decode.load()

        data = []

        for y in range(height):
            for x in range(width):

                r_encoded, g_encoded, b_encoded = encoded_image[x, y]

                r_encoded = dcdimgclass.get_n_least_significant_bits(
                    r_encoded, n_bits)
                g_encoded = dcdimgclass.get_n_least_significant_bits(
                    g_encoded, n_bits)
                b_encoded = dcdimgclass.get_n_least_significant_bits(
                    b_encoded, n_bits)

                r_encoded = dcdimgclass.shit_n_bits_to_8(r_encoded, n_bits)
                g_encoded = dcdimgclass.shit_n_bits_to_8(g_encoded, n_bits)
                b_encoded = dcdimgclass.shit_n_bits_to_8(b_encoded, n_bits)

                data.append((r_encoded, g_encoded, b_encoded))

        dcdimgclass.make_image(
            data, image_to_decode.size).save(decoded_image_path)
