import requests
from PIL import Image, UnidentifiedImageError
from io import BytesIO
import sys
from bs4 import BeautifulSoup
import tkinter as tk
import random
import tempfile

# Функция для поиска картинки в Google
def search_image(query):
    url = "https://www.google.com/search"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    params = {"q": query, "tbm": "isch", "tbs": "isz:lt,islt:2mp"}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.text
    else:
        print("Ошибка поиска: код ответа:", response.status_code)
        return None

# Функция для получения случайной картинки из поиска
def get_random_image_from_search(query):
    search_result = search_image(query)
    if search_result:
        soup = BeautifulSoup(search_result, 'html.parser')
        images = soup.find_all('img')
        if len(images) >= 3:
            # Выбираем случайное число от 2 до 49 или до конца списка изображений
            index = random.randint(2, min(len(images) - 1, 49))
            image_url = images[index]['src']
            if not image_url.startswith('http'):
                image_url = 'https://www.google.com' + image_url
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))
            return image
        else:
            print("На странице поисковой выдачи Google найдено менее трех изображений.")
            return None
    else:
        print("Не удалось найти картинку. Попробуем снова...")
        return None

# Функция для сохранения изображения во временном файле и отображения его в окне
def show_image(image):
    if image:
        try:
            # Увеличиваем размер изображения
            image = image.resize((600, 400))
            # Создаем временный файл и сохраняем изображение в нем
            with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
                image.save(tmp.name)
                tmp.close()
                img = Image.open(tmp.name)
                img.show()
        except KeyboardInterrupt:
            sys.exit(0)
        except UnidentifiedImageError:
            print("Не удалось отобразить изображение.")
    else:
        print("Картинка недоступна")

# Функция для обработки ввода пользователя
def handle_input(event=None):
    query = entry.get()
    image = get_random_image_from_search(query)
    if image:
        show_image(image)
    else:
        print("Ошибка получения картинки. Попробуем снова...")

# Создаем окно ввода
root = tk.Tk()
label = tk.Label(root, text="Введите запрос для поиска картинки:")
label.pack()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Поиск", command=handle_input)
button.pack()

# Добавляем обработчик события нажатия на клавишу "Enter"
entry.bind("<Return>", handle_input)

root.mainloop()

