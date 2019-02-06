# Categorical data vs Numerical data
'''
- Categorical data: data used only to differentiate data 
    * no need to do normalization 
    * Random Forest Method works well
    * Use the following format to better represent categorical data
        A = 1 0 0 0 
        B = 0 1 0 0 
        C = 0 0 1 0
        D = 0 0 0 1

- Numerical data: normalization necessary / various fitting classifier available
'''

# Cross validation and Grid search (refer to textbook)
'''
Cross validation
- Disjoint dataset into multiple pieces and use one of then for testig
- Repeat fitting test with each of data pieces and average out the accuracy
- Use library: model_selection.cross_val_score()

Grid search
- Parameter optimization
- Need to understand what parameters are used and set the limits
- Use library: GridSearchCV() 
'''


# downloading file from an url
'''
import urllib.request as req
local = "mushroom.csv"
url = "..."
req.urlretrieve(url, local)
'''

# Numerical Data: manipulating Pandas DataFrame and splitting data into train/test and data/label
'''
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

mr = pd.read_csv("agaricus-lepiota.data", header=None)

label = []
data = []
attr_list = []

for row_index, row in mr.iterrows():
    label.append(row.ix[0])
    row_data = []
    for v in row.ix[1:]:
        row_data.append(ord(v))
    data.append(row_data)

data_train, data_test, label_train, label_test = train_test_split(data, label)

print(data_train[0:5])
print(data_test[0:5])
print(label_train[0:5])
print(label_test[0:5])

clf = RandomForestClassifier()
clf.fit(data_train, label_train)
predict = clf.predict(data_test)
score = metrics.accuracy_score(label_test, predict)
report = metrics.classification_report(label_test, predict)

print("acc: ", score)
print("report: \n", report)

# if used with svm.SVC(), the accuracy reduces slightly
'''

# Categorical Data: converting to matrix type variables

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

mr = pd.read_csv("agaricus-lepiota.data", header=None)

label = []
data = []
attr_list = []

for row_index, row in mr.iterrows():
    label.append(row.ix[0])
    exdata = []
    for col, v in enumerate(row.ix[1:]):
        if row_index == 0:
            attr = {"dic": {}, "cnt":0}
            attr_list.append(attr)
        else:
            attr = attr_list[col]
        d = [0,0,0,0,0,0,0,0,0,0,0,0]
        if v in attr["dic"]:
            idx = attr["dic"][v]
        else:
            idx = attr["cnt"]
            attr["dic"][v] = idx
            attr["cnt"] += 1
        d[idx] = 1
        exdata += d
    data.append(exdata)

data_train, data_test, label_train, label_test = train_test_split(data, label)

print(data_train[0:5])
print(data_test[0:5])
print(label_train[0:5])
print(label_test[0:5])

clf = RandomForestClassifier()
clf.fit(data_train, label_train)
predict = clf.predict(data_test)
score = metrics.accuracy_score(label_test, predict)
report = metrics.classification_report(label_test, predict)

print("acc: ", score)
print("report: \n", report)

# if used with svm.SVC(), the accuracy reduces slightly
