IMAGE_BASE:=discord_roulette_bot

IMAGE_TAG:=latest

install: poetry.lock
	poetry install --no-root

install-dev: poetry.lock
	poetry install --with lint,test --no-root

install-lint: poetry.lock
	poetry install --with lint --without dev --no-root

install-test: poetry.lock
	poetry install --with test --no-root

install-hooks:
	cp .githooks/* .git/hooks/

lint:
	poetry run black . --check --exclude '\.venv/|\.git/' $(PARAMS)

test:
	poetry run pytest ./api/$(SERVICE)

run: install
	poetry run uvicorn main:app --reload --host 0.0.0.0

migrations:
	poetry run alembic upgrade head

build-image:
	docker build -f environments/$(ENV)/Dockerfile.$(SERVICE) -t $(IMAGE_BASE)_$(ENV)_$(SERVICE):$(IMAGE_TAG) .

build-all-images:
	make build-image SERVICE=admin ENV=$(ENV) IMAGE_BASE=$(IMAGE_BASE) IMAGE_TAG=$(IMAGE_TAG)
	make build-image SERVICE=player ENV=$(ENV) IMAGE_BASE=$(IMAGE_BASE) IMAGE_TAG=$(IMAGE_TAG)

run-image:
	docker run -d -p "8000:8000" --name $(ENV)_$(SERVICE) $(IMAGE_BASE)_$(ENV)_$(SERVICE):$(IMAGE_TAG)

push-image:
	docker push $(IMAGE_BASE)_$(ENV)_$(SERVICE):$(IMAGE_TAG)

push-all-images: 
	make push-image SERVICE=admin ENV=$(ENV) IMAGE_BASE=$(IMAGE_BASE) IMAGE_TAG=$(IMAGE_TAG)
	make push-image SERVICE=player ENV=$(ENV) IMAGE_BASE=$(IMAGE_BASE) IMAGE_TAG=$(IMAGE_TAG)
