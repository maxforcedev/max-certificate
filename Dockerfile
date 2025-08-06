# Use a imagem oficial do Python
FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip \
  && pip install -r requirements.txt

COPY . .
RUN mkdir -p /app/media /app/static
EXPOSE 8000

CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
