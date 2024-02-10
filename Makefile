IMAGE_NAME?=discord_roulette_bot
IMAGE_TAG?=latest

install: poetry.lock
	poetry install --no-root

lint:
	black .

cicd-lint:
	black . --check --exclude '\.venv/|\.git/'

test:
	pytest .

cicd-test:
	poetry run pytest .

run:
	poetry run uvicorn main:app --reload --host 0.0.0.0

build-image:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .

run-image: build-image
	docker run -p $(IMAGE_NAME):$(IMAGE_TAG) .
