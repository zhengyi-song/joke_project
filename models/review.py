import sqlite3

class ReviewModel(object):
    
    def __init__(self, review_id, review_content, review_date, user_id, joke_id):
        self.review_id      = review_id
        self.review_content = review_content
        self.review_date    = review_date
        self.user_id        = user_id
        self.joke_id        = joke_id
    
    def json(self,review_id):
        return {'review_id':review_id,
                'review_content':self.review_content,
                'review_date':self.review_date,
                'user_id':self.user_id,
                'joke_id':self.joke_id}
        
    @classmethod
    def find_by_review_id(cls,review_id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        result = cursor.execute('SELECT * FROM reviews WHERE review_id = ?',(review_id,))
        row = result.fetchone()
        connection.close()
        return cls(*row) if row else None
    
    def save_to_db(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO reviews VALUES (NULL,?,?,?,?)',
                       (self.review_content,self.review_date,self.user_id,self.joke_id)
                      )
        connection.commit()
        connection.close()
        
    def delete_from_db(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM reviews WHERE review_id = ?',(self.review_id,))
        connection.commit()
        connection.close()
    
    def update_in_db(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute('UPDATE reviews SET review_content = ?, review_date = ?, user_id = ?, joke_id = ? WHERE review_id = ?',(self.review_content, self.review_date, self.user_id, self.joke_id, self.review_id))
        connection.commit()
        connection.close()
       
        