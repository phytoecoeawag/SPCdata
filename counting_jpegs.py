#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 18:25:13 2020

@author: Tommy

This script counts how many images are in each subfolder in "home"
"""

import os
import numpy as np
import pandas as pd


home = input('directory?')


#%%
subfolders = os.listdir(home)
files_n = 0 #initiate the counter for files in the main folder
classes = [] #empty list for the classes
#Remove the hidden .DS files and the single files
for i in subfolders:
    if i.startswith('.DS') or i.endswith('Thumbs.db'):
        subfolders.remove(i)
        
#start a new for loop to not get the indexes messed up
for i in subfolders:
    #count single files in this folder
    if os.path.isfile(os.path.join(home,i)):
        files_n = files_n+1
    else: #if it is a folder (class) append it to the list
        classes.append(i)        

#make already a matrix to count in as big as the amount of classes you have
dummy = np.zeros(len(classes))
#make dictionary dummy to later transform to data frame
dummy2 = {'Class':classes,'Counts':dummy}
dummytotal = {'Class' : 'total', 'Counts':0.0}

#convert the dictionary to dataframe, to later convert it to .csv
results = pd.DataFrame(dummy2)
#append a last row for the total
results = results.append(dummytotal,ignore_index=True)
results = results.set_index('Class')

for i in classes:
    count = 0 #initiate the count
    for a,b,c in os.walk(os.path.join(home,i)):
        for j in c: #check the files, not subfolders (b)
            if j.endswith('.jpeg') or j.endswith('.jpg') :
                #this way we avoid hidden files like .DS and Thumbs.db
                count = count+1 #if its a jpeg (SPC product), count
    results.loc[i,'Counts'] = count
    results.loc['total','Counts'] += count
    
#%%
#save the results as csv on the same folder
results.to_csv(os.path.join(home,'new_count.csv')) 

    