# Веб-приложение на FastAPI (Трекер задач)

## Описание
REST API для трекера задач (аналог Trello). Реализованы CRUD для задач и списков. Используется PostgreSQL через Docker.

## Скриншоты
(Добавьте после запуска)

## Быстрый старт
1. Установите зависимости:
```
pip install -r requirements.txt
```
2. Запустите PostgreSQL через Docker:
```
docker-compose up -d
```
3. Запустите сервер:
```
uvicorn main:app --reload
```
4. Откройте http://localhost:8000/docs

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
docker-compose up --build
```
