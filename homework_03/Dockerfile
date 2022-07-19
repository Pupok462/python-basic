FROM python:3.9-buster

WORKDIR /app
COPY requirements.txt ./
RUN pip install --requirement requirements.txt

COPY project .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=8000"]





