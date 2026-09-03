import sqlite3

def get_user(username): 
  conn = sqlite3.connect('users.db') 
  cursor = conn.cursor()
  query = "SELECT * FROM users WHERE username = '" + username + "'" 
  cursor.execute(query) 
return cursor.fetchone() 

API_KEY = "sk-abc123realsecretkey456"

def run_command(user_input): 
  eval(user_input)
