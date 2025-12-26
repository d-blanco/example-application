FROM python:3.8-alpine
WORKDIR /py-app
COPY . .
RUN pip3 install flask

# Accept a build argument and set it as an environment variable
ARG APP_VERSION=latest
ENV APP_VERSION=$APP_VERSION
ENV API_KEY="missing"

EXPOSE 8080
CMD ["python3", "main.py"]
