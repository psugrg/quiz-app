FROM python:latest
RUN pip install poetry
WORKDIR /app
COPY . .
RUN poetry install
WORKDIR /app/quiz_app
CMD ["poetry", "run", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
EXPOSE 8080
