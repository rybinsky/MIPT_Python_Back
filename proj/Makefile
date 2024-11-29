IMAGE_NAME = cards_app
CONTAINER_NAME = cards_app_container

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -d --name $(CONTAINER_NAME) -p 8000:8000 $(IMAGE_NAME)

stop:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)

clean:
	docker rmi $(IMAGE_NAME)

migrate:
	docker exec -it $(CONTAINER_NAME) python hw5/manage.py makemigrations
	docker exec -it $(CONTAINER_NAME) python hw5/manage.py migrate

createsuperuser:
	docker exec -it $(CONTAINER_NAME) python hw5/manage.py createsuperuser

test:
	docker exec -it $(CONTAINER_NAME) poetry run python manage.py test

shell:
	docker exec -it $(CONTAINER_NAME) poetry run python manage.py shell

bash:
	docker exec -it $(CONTAINER_NAME) /bin/bash

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