from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    objeto = (request.args.get('objeto'))
    texto = json.dumps(objeto)
    return texto


if __name__ == '__main__':
    app.run(debug=True)
