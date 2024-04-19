from flask import Flask, render_template

app = Flask(__name__)


@app.route('/list_prof/<num>')
def bob(num):
    list = ['one', 'dog', 'seven']
    return render_template('base.html', list=list, num=num)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
