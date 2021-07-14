
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

import requests

from .constData import *


def getData(symbol):
    querystring = {"interval":"5m","symbol":symbol,"range":"1d","region":"US"}

    response = requests.request("GET", URL, headers=headers, params=querystring).json()
    return response

def processData(responseObject):
    df = pd.DataFrame.from_dict(responseObject['chart']['result'][0]['indicators']['quote'][0])
    dataset = df['close'].values
    
    dataset = dataset.reshape(-1,1)
    scaler=MinMaxScaler(feature_range=(0,1))  
    scaled_data=scaler.fit_transform(dataset)
    x_test = []
    for i in range(0,dataset.shape[0]):
        x_test.append(dataset[i])

    x_test = np.array(x_test)
    x_test=np.reshape(x_test,(x_test.shape[0],x_test.shape[1],1))
    return x_test


