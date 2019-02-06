# data = "0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	67	232	39	0	0	0	0	0	0	0	0	0	62	81	0	0	0	0	0	0	0	0	0	0	0	0	0	0	120	180	39	0	0	0	0	0	0	0	0	0	126	163	0	0	0	0	0	0	0	0	0	0	0	0	0	2	153	210	40	0	0	0	0	0	0	0	0	0	220	163	0	0	0	0	0	0	0	0	0	0	0	0	0	27	254	162	0	0	0	0	0	0	0	0	0	0	222	163	0	0	0	0	0	0	0	0	0	0	0	0	0	183	254	125	0	0	0	0	0	0	0	0	0	46	245	163	0	0	0	0	0	0	0	0	0	0	0	0	0	198	254	56	0	0	0	0	0	0	0	0	0	120	254	163	0	0	0	0	0	0	0	0	0	0	0	0	23	231	254	29	0	0	0	0	0	0	0	0	0	159	254	120	0	0	0	0	0	0	0	0	0	0	0	0	163	254	216	16	0	0	0	0	0	0	0	0	0	159	254	67	0	0	0	0	0	0	0	0	0	14	86	178	248	254	91	0	0	0	0	0	0	0	0	0	0	159	254	85	0	0	0	47	49	116	144	150	241	243	234	179	241	252	40	0	0	0	0	0	0	0	0	0	0	150	253	237	207	207	207	253	254	250	240	198	143	91	28	5	233	250	0	0	0	0	0	0	0	0	0	0	0	0	119	177	177	177	177	177	98	56	0	0	0	0	0	102	254	220	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	169	254	137	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	169	254	57	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	169	254	57	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	169	255	94	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	169	254	96	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	169	254	153	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	169	255	153	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	96	254	153	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0"
# list_data = data.split("\t")
# for i in range(len(list_data)):
#     print("{:3}".format(list_data[i]), end="")
#     if i % 28 == 0:
#         print()

from sklearn import model_selection, svm, metrics
import pandas

train_csv = pandas.read_csv("./mnist/train.csv", header = None)
tk_csv = pandas.read_csv("./mnist/t10k.csv", header = None)

# print(type(train_csv), type(tk_csv))
# print(train_csv[0].values) # train_csv is a dataframe instance
# # train_csv[0] access to first column
# # train_csv[0].values converts it to a list instance
# # train_csv.iloc[row, colunn] chooses ranges of a dataframe

train_csv_data = train_csv.iloc[:, 1:].values
train_csv_label = train_csv[0].values 
tk_csv_data = tk_csv.iloc[:, 1:].values 
tk_csv_label = tk_csv[0].values

# data used in fit has to be in [0, 1]
# using map function to convert the list

def test(l):
    output = []
    for i in l:
        output.append(float(i)/256)
    return output

train_csv_data = list(map(test, train_csv_data))
tk_csv_data = list(map(test, tk_csv_data))
# result of map function is "iterable", 
# so type-casting to "list" is necessary

clf = svm.SVC()
clf.fit(train_csv_data, train_csv_label)

predict = clf.predict(tk_csv_data)
score = metrics.accuracy_score(tk_csv_label, predict)
print("Accuracy: ", score)

cl_report = metrics.classification_report(tk_csv_label, predict)
print("Report: \n", cl_report)
