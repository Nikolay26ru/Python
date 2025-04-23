# Data Science / ML мини-проект (Анализ отзывов Ozon)

## Описание
Мини-проект по анализу тональности отзывов с Ozon. Используется pandas, scikit-learn, matplotlib.



## Быстрый старт
1. Установите зависимости:
```
pip install -r requirements.txt
```
2. Запустите ноутбук:
```
jupyter notebook analysis.ipynb
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
docker build -t ds_project .
docker run --rm ds_project
```
