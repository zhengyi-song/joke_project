from flask_restful import Resource, reqparse
from models.joke import JokeModel

class Joke(Resource):
    
    parser = reqparse.RequestParser()
    #parser.add_argument('joke_name',
    #                    type=str,
    #                    required=True,
    #                    help="This field cannot be blank."
    #                    )
    parser.add_argument('joke_content',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('joke_date',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('user_id',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )
    
    def get(self,joke_name):
        joke = JokeModel.find_by_joke_name(joke_name)
        return joke.json() if joke else None
    
    def post(self,joke_name):
        joke = JokeModel.find_by_joke_name(joke_name)
        if joke:
            return {'message':'joke with name of {} is already existing'.format(joke_name)}
        data = Joke.parser.parse_args()
        new_joke = JokeModel(None,joke_name,**data)
        new_joke.save_to_db()
        return new_joke.json()
    
    def delete(self,joke_name):
        joke = JokeModel.find_by_joke_name(joke_name)
        if not joke:
            return {'message':'joke with name of {} is not existing'.format(joke_name)}
        joke.delete_from_db()
        return {'message':'joke with name of {} is deleted'.format(joke_name)}
    
    def put(self,joke_name):
        joke = JokeModel.find_by_joke_name(joke_name)
        data = Joke.parser.parse_args()
        if not joke:
            new_joke = JokeModel(None,joke_name,**data)
            new_joke.save_to_db()
            return new_joke.json()
        else:
            new_joke = JokeModel(joke.joke_id,joke_name,**data)
            new_joke.update_in_db()
            return new_joke.json()
        