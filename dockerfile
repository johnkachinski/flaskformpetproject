FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/

RUN pip install poetry

RUN POETRY_VIRTUALENVS_CREATE=false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY . .

EXPOSE 5000

CMD ["poetry", "run", "gunicorn", "--timeout", \
"120", "--workers", "4", "--bind", "0.0.0.0:5000", "src.main:app"]