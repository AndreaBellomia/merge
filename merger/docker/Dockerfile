FROM python:3.11

ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
EXPOSE 8000
WORKDIR /app
COPY ../../../requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY ../../merger /app/airoffice

CMD ["python", "manage.py", "runserver"]