FROM python:3.6

# Copia todos los archivos del contexto actual al directorio /app3 en la imagen
COPY . /app3

# Expone el puerto 5003 en el contenedor
EXPOSE 5003

# Establece el directorio de trabajo
WORKDIR /app3

# Copia el archivo requirements.txt al contenedor y luego instala las dependencias
COPY requirements.txt /app3/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia los archivos de Python necesarios al contenedor
COPY run.py /app3
COPY config.py /app3

# Comando por defecto para ejecutar cuando el contenedor se inicie
CMD ["python", "run.py", "config.py"]

