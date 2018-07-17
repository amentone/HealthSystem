from flaskr import app, request
from flask import jsonify
import csv
import json

@app.route('/hs/pebble',methods=['GET','POST'])
def pebble():
    if request.method == 'POST':
        f = request.get_data(as_text=True)
        return  f 
    
