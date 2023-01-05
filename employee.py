from flask import Flask
from flask import jsonify, json

import sqlite3
import os
from sqlite3 import Error

app = Flask(__name__)

db_file = "employees.db"
backup_port = 5000


def get_db_connection():

    ''' 
    Ideally I would mainatain a persistent db connection so we dont 
    connect to db on every request.
    But for simplicity using this for now
    Alternative is to use sqlalchemy or some solution to persist the connection.
    '''
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


@app.route('/employees',methods=['GET'])
def getAllEmp():
    conn = get_db_connection()
    cursor = conn.execute('SELECT id, gender FROM employees')
    columns = [column[0] for column in cursor.description]

    employee_data=[]

    for row in cursor.fetchall():
        employee_data.append(dict(zip(columns, row)))

    return jsonify(employee_data)
    

if __name__ == "__main__":
    port = os.environ.get("PORT") 

    if port is None:
        print ('Env variable PORT not configured. Defaulting to ', backup_port )
        port = backup_port
    else:
        print ('Listening on port', port )

    app.run(host='localhost', port = port)

    