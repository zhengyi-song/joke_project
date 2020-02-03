from flask import Flask
from flask_restful import Api

from resources.user import User
from resources.joke import Joke
from resources.review import Review

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jeremy'
api = Api(app)

api.add_resource(Joke, '/joke/<string:joke_name>')
api.add_resource(Review, '/review/<int:review_id>')
api.add_resource(User, '/user')

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True