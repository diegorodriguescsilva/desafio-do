from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Olá, mundo! Esta é uma aplicação em Python rodando no Docker."

if __name__ == '__main__':
    print("👋 Olá, DIO! Essa é a minha pequena contribuição: uma imagem rodando no Docker.")
    app.run(host='0.0.0.0', port=5000)
