FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
EXPOSE 80
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . /app
COPY ../models /app

