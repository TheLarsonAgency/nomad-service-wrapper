"""Flask API"""

from flask import Flask

from flaskrun import flaskrun
from runner import Runner

app = Flask(__name__)  # pylint: disable=invalid-name


@app.route('/check_status')
def get_status():  # pylint: disable=missing-docstring
    return '{{"Status":"{runner.status()}"}}'


if __name__ == '__main__':
    runner = Runner()  # pylint: disable=invalid-name
    flaskrun(app)
    runner.shutdown()
