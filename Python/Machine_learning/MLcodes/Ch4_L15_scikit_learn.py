# Separating leaning/training data and test/label data 

from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import pandas as pd


csv = pd.read_csv('iris.csv')

csv_data = csv[["sepal_length", "sepal_width", "petal_length", "petal_width"]] 
csv_label = csv["species"]

train_data, test_data, train_label, test_label = \
    train_test_split(csv_data, csv_label)

clf = svm.SVC()
clf.fit(train_data, train_label)
results = clf.predict(test_data)

score = metrics.accuracy_score(results, test_label)
print("Accuracy rate", score)

'''
results = clf.predict([
    [5.1, 3.0, 1.3, 0.2],
    [5, 3, 2, 1]
])
'''