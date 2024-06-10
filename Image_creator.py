# v0.1

# !pip install pillow
# !pip install numpy

# from PIL import Image
# import random
# import numpy as np

# def generate_random_image(width, height):
#     image = Image.new("RGB", (width, height))

#     pixels = []
#     for _ in range(width * height):
#         red = random.randint(0, 255)
#         green = random.randint(0, 255)
#         blue = random.randint(0, 255)
#         pixels.append((red, green, blue))

#     image.putdata(pixels)
#     return image

# # Пример использования:
# image_width = 500
# image_height = 500
# random_image = generate_random_image(image_width, image_height)
# random_image.show()


# v0.2

# Установка библиотек
!pip install request
!pip install pillow
!pip install io

import requests
from PIL import Image
from io import BytesIO
import random

MAX_ATTEMPTS = 5

# Генерируем случайный URL картинки
def generate_random_image_url():
    # Здесь можно использовать любую другую логику для получения случайного URL
    urls = [
        "https://source.unsplash.com/random",
        "https://picsum.photos/500/500",
        "https://placeimg.com/500/500/any",
        "https://random.imagecdn.app/500/500"
    ]

    random_url = random.choice(urls)
    return random_url

# Получаем случайную картинку из интернета
def get_random_image_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        return image

    return None

# Открываем картинку в окне
def show_image(image):
    if image:
        image.show()
    else:
        print("Картинка недоступна")

# Генерируем случайный URL картинки и пытаемся получить картинку
attempts = 0
random_image_url = generate_random_image_url()
random_image = get_random_image_from_url(random_image_url)
while not random_image and attempts < MAX_ATTEMPTS:
    attempts += 1
    random_image_url = generate_random_image_url()
    random_image = get_random_image_from_url(random_image_url)

# Открываем картинку в окне (если доступно)
show_image(random_image)

