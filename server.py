from flask import Flask, render_template

app = Flask(__name__)


@app.route('/list_prof', methods=['GET', 'POST'])
def bob():
    list = requests.get('http://127.0.0.1:8080')
    return list


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
