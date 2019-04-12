# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 11:28:23 2019

@author: Bhargav Rallapalli
"""

from flask import Flask, render_template
#import requests, json 
#from pandas.io.json import json_normalize
#from sqlalchemy import create_engine
#import urllib
#import pandas as pd
#import pyodbc

app = Flask(__name__)

@app.route('/')
#@app.route('/home')
def index():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run(debug = True)


#--------------------- PYODBC CONNECTION --------------------------------#
#def create_connection():
#    connection = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=RSB\MSSQLSERVER01;DATABASE=data_Test;uid=sa;pwd=123')
#    return connection
#connection=create_connection()
#cursor = connection.cursor()
#
#for row in df.iterrows():
#    cursor.execute("INSERT INTO dbo.Places values (?,?,?,?,?,?)", row['Name'], row['Place_ID'] , row['Latitude'],row['Longitude'],row['Ratings'],row['Total_Ratings']) 
#    connection.commit()
#cursor.close()
#connection.close()

#pd.read_sql_query(sql, db)

#class Details(List_Details):
#    email = places()
#users = [Details.load(connection, uid) for uid in connection]
#
#for user in users:
#    print (user.id, user.email)
#
#@app.route("/users")
#def show_data():
#    users = [Details.load(db, uid) for uid in db]
#    return render_template('users.html', users=users)
#    

'''
#--------------------- SQL ALCHEMY DB CONNECTION --------------------------------#
params = 'DRIVER={ODBC Driver 13 for SQL Server};' \
         'SERVER=RSB\MSSQLSERVER01;' \
         'PORT=5000;' \
         'DATABASE=dataframe;' \
         'UID=sa;' \
         'PWD=123;'
            
params = urllib.parse.quote_plus(params)


db = create_engine('mssql+pyodbc:///?odbc_connect=%s' % params)
connection = db.connect()
'''
