FROM python:3.9

WORKDIR /django

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "manage.py","runserver"]