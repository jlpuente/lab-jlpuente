# imagen base
FROM python:3.10.8-slim-bullseye
# copiamos src a carpeta dentro del contenedor
COPY main.py /app/

CMD ["python", "/app/main.py"]