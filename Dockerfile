FROM python:3.12-slim

RUN pip install langchain_openai

COPY . .

CMD ["python3", "app.py"]
