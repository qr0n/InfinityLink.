from re import L
from flask import Flask
import json
from IronDB.logic import db_load
app = Flask(__name__)

@app.route('/')
def navigate():
  return db_load()



app.run()