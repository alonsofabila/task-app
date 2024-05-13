FROM python:3.12
LABEL authors="jorge"

WORKDIR /task-app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
