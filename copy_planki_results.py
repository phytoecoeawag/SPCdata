#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 15:48:28 2021

@author: Tommy

Read plankifier results and make folders with the images that resulted from 
plankifier. This is good to check the results of the plankifier.
"""


import pandas as pd
import os
import numpy as np
import shutil 

#%%Read Data

path = '/Users/ecoadmin/Documents/Time_Efficiency/raw_jpegs_planki'
#'/Users/ecoadmin/Documents/temp/test4'
#input('path?')
results_name = 'results_ver01_leaderabs0.0.txt'
#input('results name?')
#directory from the classes that the classifier used
classesdir = '/Users/ecoadmin/Documents/Annotation_Protocol/plankifier/plankifier-1.2.2/trained-models/Phyto_eff6_classifier_ver01/classes.npy'
classes = np.load(classesdir)
#folder to where you want to copy the results
dest = '/Users/ecoadmin/Documents/Time_Efficiency/planki_sorted'


for k in classes:
    
    #ctype = k
    #input('phyto class?')
    destpath = os.path.join(dest,k) 
    try: #make a directory on destination with the name of the class
        os.mkdir(destpath)
    except: #in case the directory already exists and this spits out an error
        pass
    
    for i in os.listdir(path): 
        folderpath = os.path.join(path,i)#path until timestamp i
        if os.path.isdir(folderpath): #can only do the rest if this is a folder
            for j in os.listdir(folderpath):
                if j.endswith(results_name):
                    filepath = os.path.join(folderpath,results_name)#path until .txt file with results
		    #Read the data from the results
                    data = pd.read_csv(filepath, header = None, delimiter=" ")
                    data.columns = ['Path','Result']
                    #Search for specific class in the results
                    #results in a data frame with only the rows with that class
                    ctype_df = data[data['Result'] == k]
                    for m in ctype_df['Path']: #m is the path the plankifier classified
                        shutil.copy2(m,destpath) #copy it to destpath
                        

#%% 




