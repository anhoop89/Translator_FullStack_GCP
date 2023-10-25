"""
A simple translation flask app.
"""
import flask
from flask.views import MethodView
from index import Index
from components.translate import Translate
from components.favorite import Favorite
from components.history import History

app = flask.Flask(__name__)  # Create a Flask app

app.add_url_rule('/', 
                 view_func=Index.as_view('index'), 
                 methods=['GET'])

app.add_url_rule('/translate/', 
                 view_func=Translate.as_view('translate'), 
                 methods=['GET', 'POST', 'PUT'])

app.add_url_rule('/favorite/', 
                 view_func=Favorite.as_view('favorite'), 
                 methods=['GET', 'POST', 'PUT'])

app.add_url_rule('/history/', 
                 view_func=History.as_view('history'), 
                 methods=['GET', 'POST', 'PUT'])
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, debug=True)
