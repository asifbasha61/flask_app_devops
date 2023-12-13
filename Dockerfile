FROM python:slim
WORKDIR /flask_app
COPY . .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "app.py"]

