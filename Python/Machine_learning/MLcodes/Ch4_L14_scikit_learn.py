# Main flow of machine learning

from sklearn import svm, metrics

clf = svm.SVC()

clf.fit([
    [0, 0],  # train data
    [1, 0], 
    [0, 1],
    [1, 1]
], [
    0,   # train label
    1,
    1,
    0
])

predicted_results = clf.predict([
    [0, 0],  # test data
    [1, 0]
]) 

print(predicted_results)

# score = matrics.accuracy_score(<test label>, <predicted_results>)