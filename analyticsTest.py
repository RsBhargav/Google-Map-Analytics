# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 21:54:35 2019

@author: Bhargav Rallapalli
"""

import pandas as pd
import pyodbc
import json
from flask import Flask,render_template,url_for #importing flask class
app = Flask(__name__)

output = []
def create_connecton():
    connection = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=RSB\MSSQLSERVER01;DATABASE=data_Test;uid=sa;pwd=123')
    return connection

def removNestings(l): 
    
    for i in l: 
        if type(i) == list: 
            removNestings(i) 
        else: 
            output.append(i)



@app.route("/")       # "/" - means-> root page of the website
   
@app.route("/home")                	 	
def home():
    connection = create_connecton()
    cursor=connection.cursor()
    for row in df.iterrows():
        cursor.execute("INSERT INTO dbo.Places values (?,?,?,?,?,?)", row['Name'], row['Place_ID'] , row['Latitude'],row['Longitude'],row['Ratings'],row['Total_Ratings']) 
    connection.commit()
    query='SELECT * FROM dbo.Places'
    q1=cursor.execute(query)
    items=[]

    for row in q1: 
        for key in cursor.description:
            items.append([value for value in row])
    removNestings(items)
    keys=[]
    for i in range(0,len(output)): 
        keys.append("table_name"+str(i))

    data_dict=dict(zip(keys,output))
    j=json.dumps(data_dict)
    data=[json.loads(j)]
    
    return render_template('home.html', data = data)


@app.route("/getdDetails")
def get():
    return json
if __name__ == '__main__':  # to run directly --> python <file_name.py>	
   app.run(debug=True) 

