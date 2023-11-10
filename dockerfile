# Imagen base de Python.
FROM python:3.9-alpine

# Copia el directorio del contenedor.
COPY . /sql_alchemy
WORKDIR /sql_alchemy

# Actualiza pip y instala las dependencias.
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expone el puerto del contenedor.
EXPOSE 5005

# Define variables de entorno.
ENV FLASK_APP=app/__init__.py
ENV FLASK_RUN_HOST=0.0.0.0

# Ejecuta el script al iniciar el contenedor.
CMD ["sh", "run.sh"]
