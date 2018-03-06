#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# print number of people
print "number of people = ", len(enron_data)

# print number of features for each person
name1 = enron_data.keys()
print "number of features = ", len(enron_data[name1[1]])




POIcount = 0
for name in enron_data.keys():
    if enron_data[name]["poi"] == 1:
        POIcount = POIcount + 1
print "number of people of interests = ", POIcount  #28




POInames_file = open("../final_project/poi_names.txt", "r")
POInames_data = POInames_file.readlines()
print len(POInames_data[2:])  #35
#print(POInames_data)

'''
POInames_data = POInames_file.read()
counter2 = 0
for character in POInames_data:
    if character == "(":
        counter2 = counter2 + 1
print "number of POI in name list is ", counter2
'''
# because not every POI is from Enron, and the dataset is only the sample from whole staff emails.


print enron_data['PRENTICE JAMES']['total_stock_value']
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']


print enron_data['SKILLING JEFFREY K']['total_payments']
print enron_data['LAY KENNETH L']['total_payments']
print enron_data['FASTOW ANDREW S']['total_payments']

# non-quantified values
count_salary = 0
count_email = 0
for key in enron_data.keys():
    if enron_data[key]['salary'] != 'NaN':
        count_salary+=1
    if enron_data[key]['email_address'] != 'NaN':
        count_email+=1
print "non-quantified salary number is: ", count_salary
print "non-quantified email address number is: ", count_email


# missing total payment 
nan_count = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN':
        nan_count = nan_count + 1
print "nan total payments number is: ", nan_count  #21
print "percentage of non total payments is: ", float(nan_count)/len(enron_data.keys())

# poi missing total payments:
poi_nan_count = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi'] == True :
        poi_nan_count = poi_nan_count + 1
print "nan total payments poi number is: ", poi_nan_count  #0
print "percentage of non total payments poi number is: ", float(poi_nan_count)/len(enron_data.keys())