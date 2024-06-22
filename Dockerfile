FROM python:3.12-alpine

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV DEBUG false
ENV OPENAI_API_KEY 'sk-proj-key'

COPY ./src ./src

RUN pip install --no-cache-dir -r src/requirements.txt

EXPOSE 80
CMD uvicorn src.server:app --host 0.0.0.0 --port 80
