FROM python:3.8-alpine
WORKDIR /py-app
COPY . .
RUN pip3 install flask
EXPOSE 8080
CMD ["python3", "main.py"]
