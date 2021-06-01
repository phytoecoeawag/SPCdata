#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:56:18 2021

@author: Tommy

Very similar to copy_planki_results.py

Read the output of the classifier and compare, look for specific class, 
plot the amount of images of that class for each date.

list of dates for class name.
"""


import pandas as pd
import os
from datetime import datetime 
import matplotlib.pyplot as plt
import numpy as np

#%%Read Data

path = '/Users/ecoadmin/Documents/Phyto_jpegs_timestamps'
#'/Users/ecoadmin/Documents/temp/test4'
#input('path?')
results_name = 'results_ver02_leaderabs0.5.txt'
#input('results name?')
#directory from the classes of the classifier used
classesdir = '/Users/ecoadmin/Documents/Annotation_Protocol/plankifier/plankifier-1.2.2/trained-models/Phyto_eff6_classifier_ver01/classes.npy'
classes = np.load(classesdir)

for k in classes:
    
    #ctype = k
    #input('phyto class?')
    
    dates = [] #empty list for dates with the searched class
    counts = [] #empty list for how many images on that date
    
    for i in os.listdir(path): 
        folderpath = os.path.join(path,i)#path until timestamp i
        if os.path.isdir(folderpath): #to avoid hidden files complications:
            timestamp = int(i) #i is the timestamp, convert to int
            dt_object = datetime.fromtimestamp(timestamp) #convert it to date object 
            date = dt_object.strftime("%d/%m/%Y, %H:%M:%S") #convert to date format
            for j in os.listdir(folderpath):
                if j.endswith(results_name):
                    filepath = os.path.join(folderpath,results_name)#path until .txt file with results
                    data = pd.read_csv(filepath, header = None, delimiter=" ")
                    data.columns = ['Path','Result']
                    #Search for specific class in the results
                    #results in a data frame with only the rows with that class
                    ctype_df = data[data['Result'] == k]
                    counts.append(len(ctype_df)) #append the number of images
                    dates.append(date) #append the date to the list
    
    dummy = {'Date' : dates , 'Count' : counts} #dictionary to pass it onto pandas
    results = pd.DataFrame(dummy)
    results.to_csv(os.path.join(path,'new_count_%s.csv' %k)) 
    
    #%% Plot dates
    
    x = [] #x-axis convert strings to datetime
    for l in results['Date']:
        x.append(datetime.strptime(l, "%d/%m/%Y, %H:%M:%S"))
    y = results['Count'] 
    
    fig, ax = plt.subplots()
    plt.plot_date(x,y)
    ax.xaxis.set_tick_params(rotation=30, labelsize=10)
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.title(k) #the class type
    #save the figure,too
    plt.savefig(os.path.join(path,'new_count_%s.png' %k))
    #close to not consume too much memory 
    plt.close('all')
                    
    
    #Make one HUGE dataframe with all results? 
    #Or after searching for specific class count how many on that day


#%% 




