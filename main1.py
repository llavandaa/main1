!pip install pillow
!pip install numpy

from PIL import Image
import random
import numpy as np

def generate_random_image(width, height):
    image = Image.new("RGB", (width, height))

    pixels = []
    for _ in range(width * height):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        pixels.append((red, green, blue))

    image.putdata(pixels)
    return image

# Пример использования:
image_width = 500
image_height = 500
random_image = generate_random_image(image_width, image_height)
random_image.show()
