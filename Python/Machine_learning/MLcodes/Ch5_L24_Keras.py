# reading modules
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.callbacks import EarlyStopping
import pandas as pd, numpy as np

# data preparation
'''
[
    [<height>/200, <weight>/100], #0.0~1.0 normalization required
    [<height>/200, <weight>/100],
    [<height>/200, <weight>/100]
]

[
    'thin',     # [1, 0, 0]
    'normal',   # [0, 1, 0] 
    'fat'       # [0, 0, 1]
]
'''
csv = pd.read_csv("bmi.csv")
csv["weight"] /= 100
csv["height"] /= 200

bmi_class ={
    'thin': [1, 0, 0], 
    'normal': [0, 1, 0], 
    'fat': [0, 0, 1]
}
y = np.empty((20000, 3))  # creating a list of 20000 items of [0, 0, 0] 

for i, v in enumerate(csv["label"]):
    y[i] = bmi_class[v]

x = csv[['weight', 'height']].as_matrix() # Convert the frame to its Numpy-array representation

x_train, y_train = x[1:15001], y[1:15001]
x_test, y_test = x[15001:20001], y[15001:20001]
# Check the size of the csv file with $ wc -l bmi.csv or $ cat -n bmi.csv

# Creation of the model
model = Sequential()

# Creation of layers
model.add(Dense(512, input_shape=(2,)))
model.add(Activation('relu'))
model.add(Dropout(0.1))

model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.1))

model.add(Dense(3))
model.add(Activation('softmax'))

model.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=['accuracy']) # refer to the documentation

# Training
model.fit(x_train, y_train,
    batch_size=100,
    nb_epoch=20,
    validation_split=0.1,
    callbacks=[EarlyStopping(monitor='val_loss', patience=2)],
    verbose=1
)

# Prediction
score = model.evaluate(x_test, y_test)
print("score: ", score)