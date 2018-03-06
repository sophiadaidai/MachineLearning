#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    squared_error = (predictions - net_worths)**2
    clean_data = zip(ages, net_worths, squared_error)
    clean_data = sorted(clean_data,key = lambda x: x[2][0], reverse = True)
    index = int(0.1*len(clean_data))
    
    cleaned_data = clean_data[index:]
    return cleaned_data

