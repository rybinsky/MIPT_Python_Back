# Используем официальный образ Python в качестве базового образа
FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта
COPY pyproject.toml poetry.lock ./

# Устанавливаем Poetry
RUN pip install poetry

# Устанавливаем зависимости с помощью Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Копируем весь проект в контейнер
COPY . .

# Открываем порт, на котором будет работать приложение
EXPOSE 8000

# Запускаем Django сервер
CMD ["python", "hw5/manage.py", "runserver", "0.0.0.0:8000"]