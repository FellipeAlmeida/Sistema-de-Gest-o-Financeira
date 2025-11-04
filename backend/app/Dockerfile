FROM python:3.12

WORKDIR /app
COPY app/requirements.txt .

RUN pip install -r requirements.txt

COPY app app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]