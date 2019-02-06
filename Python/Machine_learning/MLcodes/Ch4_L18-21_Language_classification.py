from sklearn import svm, metrics
import glob, os.path, re, json
import matplotlib.pyplot as pyplot
import pandas as pd

files = glob.glob("./sources/ch4/lang/train/*.txt") # getting filenames with relative path
train_data = []
train_label = []

for file_name in files: 
    basename = os.path.basename(file_name) # getting only file name
    lang = basename.split("-")[0]
    file = open(file_name, "r", encoding="utf-8")
    text = file.read()
    text = text.lower() # converts to lower characters
    file.close()

    # getting alphabet frequency
    code_a = ord("a") # ord() converts char to a number
    code_z = ord("z")
    count = [0 for n in range(0,26)] # generages 26 zeros

    for character in text:
        code_current = ord(character)
        if code_a <= code_current <= code_z:
            count[code_current - code_a] += 1
    # print(lang, count)
    total = sum(count)
    count = list(map(lambda n: n/total, count))
    train_label.append(lang)
    train_data.append(count)

files = glob.glob("./sources/ch4/lang/test/*.txt") # getting filenames with relative path
test_data = []
test_label = []

for file_name in files: 
    basename = os.path.basename(file_name) # getting only file name
    lang = basename.split("-")[0]
    file = open(file_name, "r", encoding="utf-8")
    text = file.read()
    text = text.lower() # converts to lower characters
    file.close()

    # getting alphabet frequency
    code_a = ord("a") # ord() converts char to a number
    code_z = ord("z")
    count = [0 for n in range(0,26)] # generages 26 zeros

    for character in text:
        code_current = ord(character)
        if code_a <= code_current <= code_z:
            count[code_current - code_a] += 1
    # print(lang, count)
    total = sum(count)
    count = list(map(lambda n: n/total, count))
    test_label.append(lang)
    test_data.append(count)

clf = svm.SVC()
# choose various "scikit learn classifier" from library (refer to https://scikit-learn.org)
# e.g., clf = RandomForestClassifier()

clf.fit(train_data, train_label)

predict = clf.predict(test_data)
ac_score = metrics.accuracy_score(test_label, predict)
print("Accuracy: ", ac_score)

# in the textbook, there is a code for saving the trained data to JSON file 

graph_dict = {}
for i in range(0, len(train_label)):
    label = train_label[i]
    data = train_data[i]
    if not (label in graph_dict):
        graph_dict[label] = data

asclist = [[chr(n) for n in range(97, 97+26)]]
df = pd.DataFrame(graph_dict, index=asclist) # index = row, columns = columns

pyplot.style.use('ggplot')
df.plot(kind="bar", subplots=True, ylim=(0, 0.15))
pyplot.savefig("lang-plot.png")

###
# in console, without GUI, execute: $ export MPLBACKEND="agg"
###


'''
----------------------
On Web application 
refer to the textbook Ch4.4
----------------------

#!/usr/bin/env python3
print("Content-Type: text/html; charset=utf-8")

# The first two lines above has to be included
# $ python3 -m http.server --cgi 8080
# this command should be executed in directory that contains /cgi-bin

# In case docker, run the docker command: 
# docker run -it -v $HOME:$HOME -p 8080:8080 <imagename>:<tag>
# files have to be executable (e.g., using chmod +x <file>)

print("")
print("<h1>Hello World...!</h1>")

----------------------
Compatibility
----------------------
- if a file is imported form Windows, it has to be converted
- may use $ apt-get install dos2unix; dos2unix <file>
'''