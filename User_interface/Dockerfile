FROM python:3.8
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8501
COPY . ./
COPY ../models /app

ENTRYPOINT ["streamlit", "run"]

CMD ["streamlit.py"]

