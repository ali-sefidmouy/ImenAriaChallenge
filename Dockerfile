FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
ENV AUTHOR="Ali"
EXPOSE 8000
ENTRYPOINT ["./django-entrypoint.sh"]
