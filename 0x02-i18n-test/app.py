"""Flask app instantiation"""
from flask import Flask, render_template, request
from flask_babel import Babel, _, lazy_gettext as _l
from config import Config

app = Flask(__name__)
app.config['LANGUAGES'] = Config.LANGUAGES


babel = Babel(app)


@babel.localeselector
def get_local_selector():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'])
def home():
    """Home endpoint"""

    context = {
        "message": _("Hi there!, How are you today? When will the judgement be delivered?"),
        "charges": [i for i in range(1, 10)]
    }

    return render_template('0-index.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)