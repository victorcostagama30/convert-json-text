from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    objeto = request.args.get('objeto')..decode('utf-8')
    texto = json.loads(objeto)
    return texto


if __name__ == '__main__':
    app.run()
