from flask import Flask, request, redirect, url_for, flash, jsonify

import numpy as np
import pandas as pd

import datetime
import os
import json
from Utils.prepareData import *
from Utils.processPrediction import getPrediction

app = Flask(__name__)

@app.route('/')
def mainPage():
    return 'Hi guy, you enter wrong route to prediction'

@app.route('/prediction/<string:symbol>')
def predictStock(symbol='AAL'):
    
    reponse = getData(symbol)
    vec_test = processData(reponse)
    stockPredicted = getPrediction(vec_test)
    stockPredicted = stockPredicted.tolist()
    return {'listStockPredicted': json.dumps(stockPredicted)}

if __name__ == '__main__':
    app.run()
