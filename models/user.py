import sqlite3

class UserModel(object):
    
    def __init__(self, user_id , username, password, first_name, last_name, gender, age, email):
        self.user_id    = user_id
        self.username   = username
        self.password   = password
        self.first_name = first_name
        self.last_name  = last_name
        self.gender     = gender
        self.age        = age
        self.email      = email
        
    @classmethod
    def find_by_user_id(cls,user_id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        result = cursor.execute('SELECT * FROM users WHERE user_id = ?',(user_id,))
        row = result.fetchone()
        connection.close()
        return cls(*row) if row else None #use [1:] to avoid parsing user_id
    
    @classmethod
    def find_by_username(cls,username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        result = cursor.execute('SELECT * FROM users WHERE username = ?',(username,))
        row = result.fetchone()
        connection.close()
        return cls(*row) if row else None
    
    def save_to_db(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO users VALUES (NULL,?,?,?,?,?,?,?)',(self.username, self.password, self.first_name, self.last_name, self.gender, self.age, self.email))
        connection.commit()
        connection.close()
        
  