from flask import Flask
import randomname

app = Flask(__name__)
name = randomname.get_name(adj='emotions', noun='astronomy')


@app.route('/api/v1/hello', methods=['GET'])
def hello():
    return f"Hello, my name is {name}"


if __name__ == '__main__':
    app.run(port=80, host="0.0.0.0")
