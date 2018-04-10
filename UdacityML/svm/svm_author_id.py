#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import svm


#clf = svm.SVC(kernel = "linear")
clf = svm.SVC(C = 10000, kernel = "rbf")

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t1, 3), "s"

print sum(pred)

acc = clf.score(features_test, labels_test)
print acc


'''

features_train_small = features_train[:len(features_train)/100] 
labels_train_small = labels_train[:len(labels_train)/100]

#clf1 = svm.SVC(kernel = "linear")
#clf1 = svm.SVC(kernel = "rbf")
#clf1 = svm.SVC(C = 10, kernel = "rbf")
#clf1 = svm.SVC(C = 100, kernel = "rbf")
#clf1 = svm.SVC(C = 1000, kernel = "rbf")
clf1 = svm.SVC(C = 10000, kernel = "rbf")

t2 = time()
clf1.fit(features_train_small, labels_train_small)
print "training time:", round(time()-t2, 3), "s"

t3 = time()
pred1 = clf1.predict(features_test)
print "predicting time:", round(time()-t3, 3), "s"

print pred1[10]
print pred1[26]
print pred1[50]

acc_small = clf1.score(features_test, labels_test)
print acc_small
'''
#########################################################


