FROM python:3.12-slim

WORKDIR /app

RUN pip install langchain_openai
RUN pip install streamlit

COPY . .

CMD ["streamlit", "run", "app.py"]
