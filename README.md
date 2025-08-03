# desafio-do-DIO

# 👋 Olá, DIO!

Essa é a minha pequena contribuição para esse dasfio: uma mensagem simples de aplicação Python rodando dentro de um container Docker.  
O objetivo é mostrar como empacotar uma aplicação Flask em uma imagem Docker e executá-la localmente.

---

## 🚀 Tecnologias usadas

- Python 3.10
- Flask
- Docker

---

## 📁 Estrutura do projeto

```
docker-hello-app/
├── Dockerfile
└── app.py
```

## ⚙️ Como executar localmente com Docker

### 1. Clone o repositório

```
git clone git@github.com:diegorodriguescsilva/desafio-do.git
```

### 2. Crie um arquivo ```app.py```

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Olá, mundo! Esta é uma aplicação em Python rodando no Docker."

if __name__ == '__main__':
    print("👋 Olá, DIO! Essa é a minha pequena contribuição: uma imagem rodando no Docker.")
    app.run(host='0.0.0.0', port=5000)

```

### 3. Crie o Dockerfile

```
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
```

### 4. Build da imagem Docker

```
docker build -t hello-docker-app .
```
### 3. Execute o container

```
docker run -d -p 8080:5000 hello-docker-app
```
### 4. Acesse no navegador
http://localhost:8080

# 💡 Resultado esperado

Ao acessar no navegador, você verá:
"Olá, mundo! Esta é uma aplicação em Python rodando no Docker."
Nos logs do container:
"👋 Olá, DIO! Essa é a minha pequena contribuição: uma imagem rodando no Docker."


