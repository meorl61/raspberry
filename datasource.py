def sayHellow():
    print("Hello")

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_table(conn):
    # """ 三個" 表示多行, 
    sql_projects = """  
    CREATE TABLE IF NOT EXISTS led (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		date TEXT NOT NULL,
		state INTEGER NOT NULL
    );
    """

    try:
        cursor = conn.cursor()
        cursor.execute(sql_projects)
        print("Table created successfully")
    except Error as e:
        print(e)

#def insert_data(conn, state):
def insert_data(state):    
    conn = create_connection('iot.db')
    create_table(conn)

    sql_insert = """ INSERT INTO led(date, state)
              VALUES(datetime('now','localtime'),?) """
    cur = conn.cursor()
    cur.execute(sql_insert, (state,))  #tuple寫法, 只有一個值時,最後要加逗點
    conn.commit()
    conn.close()