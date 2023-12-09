FROM python:3.9.5

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY app.py model_2.h5 ./
COPY templates /app/templates

EXPOSE 5000

CMD ["python", "app.py"]
