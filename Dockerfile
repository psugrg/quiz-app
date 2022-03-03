FROM python:latest
# RUN pip install poetry
RUN pip install fastapi uvicorn
WORKDIR /app
COPY . .
# RUN poetry install
WORKDIR /app/quiz_app
# CMD ["poetry" "run" "uvicorn", "main:app", "--reload", "--port 8080"]
CMD ["uvicorn", "main:app", "--reload", "--port 8080"]
EXPOSE 8080
