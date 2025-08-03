# Imagem base
FROM python:3.10-slim

# Diretório de trabalho
WORKDIR /app

# Copia os arquivos para a imagem
COPY . .

# Instala Flask
RUN pip install flask

# Expõe a porta do container
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
