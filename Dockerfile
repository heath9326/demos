FROM python:3.10
# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED 1
# Устанавливает рабочий каталог контейнера — "app"
WORKDIR /app
# Копирует все файлы из нашего локального проекта в контейнер
ADD ./project01 /app
COPY ./requirements.txt requirements.txt
# Запускает команду pip install для всех библиотек, перечисленных в requirements.txt

RUN pip install -r requirements.txt


CMD ["python", "manage.py", "runserver"]