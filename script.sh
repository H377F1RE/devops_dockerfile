#!/bin/bash
docker rm -f flask_app db
docker run -d \
  --name db \
  -e POSTGRES_DB=users_db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -v $(pwd)/init_db.sql:/docker-entrypoint-initdb.d/init_db.sql \
  -p 5432:5432 \
  postgres:17

docker build -t flask-app .

docker run -d \
  --name flask_app \
  --link db:db \
  -p 5000:5000 \
  -e POSTGRES_HOST=db \
  -e POSTGRES_DB=users_db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  flask-app

echo "Open http://localhost:5000"
