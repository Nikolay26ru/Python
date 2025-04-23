# Telegram-бот (Учёт задач)

## Описание
Асинхронный Telegram-бот для учёта задач. Сохраняет задачи в SQLite. Позволяет добавлять, удалять, просматривать задачи.


## Быстрый старт
1. Установите зависимости:
```
pip install -r requirements.txt
```
2. Укажите токен Telegram-бота в .env
3. Запустите:
```
python bot.py
```

## Тесты
```
pytest
```

## Форматирование
```
black .
flake8 .
```

## Docker
```
docker build -t telegram_bot .
docker run --rm telegram_bot
```
