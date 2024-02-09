FROM python:3.10-buster

ENV POETRY_VERSION=1.7.1

WORKDIR /usr/src/app
EXPOSE 8000

RUN pip install "poetry==$POETRY_VERSION"

COPY poetry.lock pyproject.toml /usr/src/app/
RUN poetry install --no-interaction

COPY . .
CMD [ "poetry", "run", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
