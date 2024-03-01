import telegram
from dotenv import dotenv_values
from time import sleep
from telegram.error import NetworkError
import argparse
from help_functions import collect_images



def send_to_bot(dir_name, time_sleep):
    while True:
        try:
            bot = telegram.Bot(token=telegram_token)
            bot.send_photo(chat_id=telegram_chat_id, photo=collect_images(dir_name))
            sleep(time_sleep)
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
    parser.add_argument(
        "-t",
        "--time_sleep",
        type=int,
        help="Время через которое происходят публикации (По умолчанию : 14400, число вводится в секундах : Пример - 4 часа = 240 минут или 14400 секунд)",
        default=14400,
    )
    args = parser.parse_args()
    dir_name = args.dir_name
    time_sleep = args.time_sleep
    send_to_bot(dir_name, time_sleep)
