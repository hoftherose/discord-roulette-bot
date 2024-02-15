IMAGE_NAME?=discord_roulette_bot
IMAGE_TAG?=latest

install: poetry.lock
	poetry install --no-root

install-lint: poetry.lock
	poetry install --with lint --without dev --no-root

install-test: poetry.lock
	poetry install --with test --without dev --no-root

lint:
	poetry run black . --check --exclude '\.venv/|\.git/'

test:
	poetry run pytest .

run: install
	poetry run uvicorn main:app --reload --host 0.0.0.0

build-image:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .

run-image: build-image
	docker run -p $(IMAGE_NAME):$(IMAGE_TAG) .
