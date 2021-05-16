# pip install mysql-connector-python

import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector(host='localhost',user='root',password='Manojbhavna01#',database='python_test')
        


