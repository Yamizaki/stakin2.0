# Usa una imagen base de Python
FROM python:3.10-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de dependencias
COPY requirements.txt . 

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Instalar TailwindCSS y dependencias de npm
WORKDIR /app/theme/static_src
RUN npm install -D tailwindcss postcss autoprefixer

# Volver al directorio de la app
WORKDIR /app

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
# Exponer el puerto de Django
EXPOSE 8000

# Ejecutar Gunicorn para servir la app
CMD ["/entrypoint.sh"]

