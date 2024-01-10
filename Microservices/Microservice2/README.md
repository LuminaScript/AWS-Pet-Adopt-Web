# 6156-microservice2

```bash

uvicorn main:app --reload
docker build -t 6156 .
docker run -d -p 80:80 6156

kill [id]


curl -X POST http://127.0.0.1:8000/adopter/create 
```