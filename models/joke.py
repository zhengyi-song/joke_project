import sqlite3

class JokeModel(object):
    
    def __init__(self, joke_id, joke_name, joke_content, joke_date, user_id):
        self.joke_id      = joke_id
        self.joke_id      = joke_id
        self.joke_name    = joke_name
        self.joke_content = joke_content
        self.joke_date    = joke_date
        self.user_id      = user_id
    
    def json(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        result = cursor.execute('SELECT joke_id FROM jokes WHERE joke_name = ?',(self.joke_name,)).fetchone()[0]
        connection.close()
        return {'joke_id':result,
                'joke_name':self.joke_name,
                'joke_content':self.joke_content,
                'joke_date':self.joke_date,
                'user_id':self.user_id}
        
    @classmethod
    def find_by_joke_id(cls,joke_id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        result = cursor.execute('SELECT * FROM jokes WHERE joke_id = ?',(joke_id,))
        row = result.fetchone()
        connection.close()
        return cls(*row) if row else None
    
    @classmethod
    def find_by_joke_name(cls,joke_name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        result = cursor.execute('SELECT * FROM jokes WHERE joke_name = ?',(joke_name,))
        row = result.fetchone()
        connection.close()
        return cls(*row) if row else None
    
    def save_to_db(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO jokes VALUES (NULL,?,?,?,?)',
                       (self.joke_name,self.joke_content,self.joke_date,self.user_id)
                      )
        connection.commit()
        connection.close()
        
    def delete_from_db(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM jokes WHERE joke_id = ?',(self.joke_id,))
        connection.commit()
        connection.close()
    
    def update_in_db(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute('UPDATE jokes SET joke_name = ?, joke_content = ?, joke_date = ?, user_id = ? WHERE joke_id = ?',(self.joke_name,self.joke_content,self.joke_date,self.user_id,self.joke_id))
        connection.commit()
        connection.close()
       
        