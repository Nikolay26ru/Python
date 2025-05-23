# Веб-скрапер (Парсер новостей РИА Новости)

## Описание
Простой парсер новостей с сайта РИА Новости. Сохраняет заголовки и ссылки в базу данных SQLite, поддерживает экспорт в CSV.

## Быстрый старт

1. Клонируйте репозиторий или скачайте проект.
2. Установите зависимости:
```
pip install -r requirements.txt
```
3. Запустите парсер:
```
python scraper.py
```
4. Проверьте базу данных `news.db` или экспортируйте данные в CSV.

## Тесты
```
pytest
```

## Форматирование кода
```
black .
flake8 .
```

## Docker
```
docker build -t web_scraper .
docker run --rm web_scraper
```
