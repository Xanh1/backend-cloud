FROM python:3.13.1-alpine

WORKDIR /flask-app

COPY . .

RUN pip install -r requirements.text

EXPOSE 8000

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]
