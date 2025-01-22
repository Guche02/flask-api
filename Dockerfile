# syntax=docker/dockerfile:1
FROM python:3.9-slim
WORKDIR /application
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "application/main.py"]


