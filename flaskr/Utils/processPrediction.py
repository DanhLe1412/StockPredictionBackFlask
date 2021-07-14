from tensorflow import keras

def getPrediction(vec):

    model = keras.models.load_model('./MLmodels/saved_lstm_model.h5')
    result = model.predict(vec)
    return result
