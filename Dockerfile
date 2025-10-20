FROM python:slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
ENV POSTGRES_HOST=db
ENV POSTGRES_DB=users_db
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
CMD ["python", "app.py"]
