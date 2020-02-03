from flask_restful import Resource, reqparse
from models.review import ReviewModel

class Review(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('review_content',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('review_date',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('user_id',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('joke_id',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )
    
    def get(self,review_id):
        review = ReviewModel.find_by_review_id(review_id)
        return review.json(review_id) if review else None
    
    def post(self,review_id):
        review = ReviewModel.find_by_review_id(review_id)
        if review:
            return {'message':'review with id of {} is already existing'.format(review_id)}
        data = Review.parser.parse_args()
        new_review = ReviewModel(None,**data)
        new_review.save_to_db()
        return new_review.json(review_id)
    
    def delete(self,review_id):
        review = ReviewModel.find_by_review_id(review_id)
        if not review:
            return {'message':'review with id of {} is not existing'.format(review_id)}
        review.delete_from_db()
        return {'message':'review with id of {} is deleted'.format(review_id)}
    
    def put(self,review_id):
        review = ReviewModel.find_by_review_id(review_id)
        data = Review.parser.parse_args()
        if not review:
            new_review = ReviewModel(None,**data)
            new_review.save_to_db()
            return new_review.json(review_id)
        else:
            new_review = ReviewModel(review_id,**data)
            new_review.update_in_db()
            return new_review.json(review_id)
        