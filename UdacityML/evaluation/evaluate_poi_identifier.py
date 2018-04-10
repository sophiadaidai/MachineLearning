#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(features, labels)
print "accuracy = ", clf.score(features, labels)


# train-test validation
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 42)
clf.fit(features_train, labels_train)
#print data_train.shape
pred = clf.predict(features_test)
print "test accuracy = ", clf.score(features_test, labels_test)
print "predict number of POI = ", sum(pred)
print "total people in test = ", len(pred)
print "if predict all 0, then test accuray = ", (len(pred) - sum(pred)) / len(pred)

import pandas as pd
result = pd.DataFrame({'pred':pred, 'actual' :labels_test})

from sklearn.metrics import precision_score
print "precision score = ", precision_score(labels_test, pred)
from sklearn.metrics import recall_score
print "recall score = ", recall_score(labels_test, pred)
