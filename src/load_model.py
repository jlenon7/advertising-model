from os.path import exists

import tensorflow.keras.models as keras
from tensorflow.keras.layers import Dense

def load_model():
  model_exists = exists('storage/advertising-model.keras')

  if (model_exists):
    print('loading advertising-model.keras')
    return keras.load_model('storage/advertising-model.keras')

  print('creating new model')
  model = keras.Sequential()

  model.add(Dense(4, activation='relu'))
  model.add(Dense(4, activation='relu'))
  model.add(Dense(4, activation='relu'))
  model.add(Dense(1))

  model.compile(optimizer='rmsprop', loss='mse')

  return model
