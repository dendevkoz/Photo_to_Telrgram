import telegram
import os
from dotenv import dotenv_values
from time import sleep
from telegram.error import NetworkError
import argparse


def send_to_bot():
    while True:
        for root_folder, folder, file in os.walk(dir_name):
            for file_name in file:
                image_path = os.path.join(f"{root_folder}", f"{file_name}")
                with open(image_path, "rb") as image_file:
                    photo = image_file.read()
                try:
                    bot = telegram.Bot(token=telegram_token)
                    bot.send_photo(chat_id=telegram_chat_id, photo=photo)
                    sleep(14400)
                except NetworkError:
                    print("Ошибка подключения. Повторная попытка через 10 секунд...")
                    sleep(10)


if __name__ == "__main__":
    telegram_token = dotenv_values(".env")["TELEGRAM_TOKEN"]
    telegram_chat_id = dotenv_values(".env")["TG_CHAT_ID"]
    parser = argparse.ArgumentParser(
        description="Загрузка изображений в Телеграм"
    )
    parser.add_argument(
        "-d",
        "--dir_name",
        type=str,
        help="Имя директории откуда будут загружаться картинки (По умолчанию : images)",
        default="images",
    )
    args = parser.parse_args()
    dir_name = args.dir_name
    send_to_bot()
