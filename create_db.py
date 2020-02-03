import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS users '+
               '( '+
               'user_id INTEGER PRIMARY KEY, '+
               'username TEXT, '+
               'password TEXT, '+
               'first_name TEXT, '+
               'last_name TEXT, '+
               'gender TEXT, '+
               'age INT, '+
               'email TEXT '+
               ')')
cursor.execute('CREATE TABLE IF NOT EXISTS jokes '+
               '( '+
               'joke_id INTEGER PRIMARY KEY, '+
               'joke_name TEXT, '+
               'joke_content TEXT, '+
               'joke_date TEXT, '+
               'user_id INT '+
               ')')
cursor.execute('CREATE TABLE IF NOT EXISTS reviews '+
               '( '+
               'review_id INTEGER PRIMARY KEY, '+
               'review_content TEXT, '+
               'review_date TEXT, '+
               'user_id INT, '+
               'joke_id INT '+
               ')')
cursor.execute('CREATE TABLE IF NOT EXISTS tags '+
               '( '+
               'joke_id INT, '+
               'tag TEXT '+
               ')')

connection.commit()
connection.close()
               
               