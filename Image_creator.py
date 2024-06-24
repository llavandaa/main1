import requests
from PIL import Image
import PIL
from io import BytesIO
import random
import time
import sys

MAX_ATTEMPTS = 5

# Генерируем случайный URL картинки
def generate_random_image_url():
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
    attempts = 0
    while attempts < 3:  # повторяем до 3 раз
        response = requests.get(url)
        if response.status_code == 200:
            if response.headers.get('Content-Type').startswith('image/'):
                try:
                    image = Image.open(BytesIO(response.content))
                    return image
                except PIL.UnidentifiedImageError:
                    print("Не удалось идентифицировать изображение. Попробуем снова...")
                    attempts += 1
                    time.sleep(1)  # ждем 1 секунду перед повторной попыткой
            else:
                print("Содержимое ответа не является изображением. Попробуем снова...")
                attempts += 1
                time.sleep(1)  # ждем 1 секунду перед повторной попыткой
        else:
            print("Не удалось получить изображение. Код статуса: ", response.status_code)
            attempts += 1
            time.sleep(1)  # ждем 1 секунду перед повторной попыткой
    return None

# Открываем картинку в окне
def show_image(image):
    if image:
        image.show()
        while True:
            try:
                image.show()
            except KeyboardInterrupt:
                sys.exit(0)
    else:
        print("Картинка недоступна")

# Функция для генерации картинки по запросу пользователя
def generate_image_on_request():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        attempts += 1
        random_image_url = generate_random_image_url()
        random_image = get_random_image_from_url(random_image_url)
        if random_image:
            show_image(random_image)
            break
        else:
            print("Ошибка получения картинки. Попробуем снова...")

# Запрашиваем у пользователя, хочет ли он увидеть картинку
while True:
    user_input = input("Хотите увидеть случайную картинку? (y/n): ")
    if user_input.lower() == 'y':
        generate_image_on_request()
        sys.exit(0)  # завершаем программу после закрытия окна с картинкой
    elif user_input.lower() == 'n':
        print("Ок, до свидания!")
        break
    else:
        print("Неправильный ввод. Попробуйте снова...")
