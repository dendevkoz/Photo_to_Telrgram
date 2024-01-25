# Photo_to_Telrgram

Данная программа позволяет скачивать фотографии и выкладывать их в Телеграм канал.

## Как установить 

Для начала вам необходимо выполнить несколько шагов:
- Зарегистрироваться на сайте [NASA](https://api.nasa.gov/) и сгенерировать токен.
- Cоздать бота в Telegram[(Создаем бот в телеграм)](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/)
- Создать канал в Telegram и назначить бота Администратором.
  
```
[Python3](https://www.python.org/downloads/) должен быть уже установлен.
```
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

## Как работает
- Для начала нужно создать файл `.env` и записать в него настройки:
    -NASA_KEY = "Ваш API ключ NASA"
    - TELEGRAM_TOKEN = "Ваш Телеграм токен"
    - CHAT_ID="ID вашего чата"
    - POST_TIME="Время задержки между постами"
    
- Для скачивания фотографий с сайта NASA запустите `fetch_nasa.py`
- Для скачивания фотографий с сайта SPACEX запустите `fetch_spacex_last_launch.py`
- Что бы выложить изображения в телеграм запустите скрипт `main.py`

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).


