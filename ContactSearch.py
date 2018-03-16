from flask import Flask, render_template
import json
import os

project_dir = os.path.dirname(os.path.realpath(__file__))
file_path = project_dir + "/data.json"

app = Flask(__name__)


@app.route('/')
def start():
    with open(file_path, 'r') as file:
        data = json.load(file)
    print(data)

    return render_template('base.html', data=data)


if __name__ == '__main__':
    app.run()
