# Переменные
IMAGE_NAME = cards_app
CONTAINER_NAME = cards_app_container

# Сборка образа Docker
build:
	docker build -t $(IMAGE_NAME) .

# Запуск контейнера Docker
run:
	docker run -d --name $(CONTAINER_NAME) -p 8000:8000 $(IMAGE_NAME)

# Остановка и удаление контейнера
stop:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)

# Удаление образа Docker
clean:
	docker rmi $(IMAGE_NAME)

# Запуск миграций
migrate:
	docker exec -it $(CONTAINER_NAME) python hw5/manage.py makemigrations
	docker exec -it $(CONTAINER_NAME) python hw5/manage.py migrate

# Создание суперпользователя
createsuperuser:
	docker exec -it $(CONTAINER_NAME) python hw5/manage.py createsuperuser

# Запуск тестов
test:
	docker exec -it $(CONTAINER_NAME) poetry run python manage.py test

# Запуск shell
shell:
	docker exec -it $(CONTAINER_NAME) poetry run python manage.py shell

# Запуск bash в контейнере
bash:
	docker exec -it $(CONTAINER_NAME) /bin/bash

# Помощь
help:
	@echo "Доступные команды:"
	@echo "  make build            - Сборка образа Docker"
	@echo "  make run              - Запуск контейнера Docker"
	@echo "  make stop             - Остановка и удаление контейнера"
	@echo "  make clean            - Удаление образа Docker"
	@echo "  make migrate          - Запуск миграций"
	@echo "  make createsuperuser  - Создание суперпользователя"
	@echo "  make test             - Запуск тестов"
	@echo "  make shell            - Запуск Django shell"
	@echo "  make bash             - Запуск bash в контейнере"
	@echo "  make help             - Показать эту справку"