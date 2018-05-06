#pip install: #mysql-connector-python

import mysql.connector
config = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'setinal',
  'raise_on_warnings': True,
  'use_pure': False,
}

def getConnection():
    try:
        return mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        raise mysql.connector.Error(str(err))

def execute(cursor,statement):
    try:
        cursor.execute(statement)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        raise mysql.connector.Error(str(err))