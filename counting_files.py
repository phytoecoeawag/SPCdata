# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:22:00 2020

@author: Tommy

the script counting_jpegs.py is clearer, more elegant and better. This was like a draft

The Results are a little off  when inside a class folder there were more subfolders. 
This is because sometimes the code reads an extra "Thumbnail" (=Thumbs.db) file, I think...
   
Will work on it. The whole counting can probably be done with only one os.walk-for-loop

Change the Path where you want to save the file. Last code line

"""
import os
#import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
#import xlrd


##Initiate variables
directory = input("directory?")
folders = []
singlefiles = []
count_singlefiles = 0

#%%

for subdirs in os.listdir(directory):
    if os.path.isdir(os.path.join(directory,subdirs)): ##if subdirs is a directory (=folders) append it to folders_list
        folders.append(subdirs)
    elif os.path.isfile(os.path.join(directory,subdirs)): ##if subdirs is a file (=.jpg or so) append it to singlefiles_list
        singlefiles.append(subdirs)
print("There are %s single files in this folder" %len(singlefiles))
print("There are %s subfolders in this folder" %len(folders))

##Create a DataFrame with the results. Better than to print everything
dummy = np.zeros([len(folders)+2,2])
results_df = pd.DataFrame(dummy,columns=['Class','Number_of_files'])
results_df.iloc[0,:] = ['single_files',len(singlefiles)]
results_df.iloc[1,:] = ['subfolders',len(folders)]

for i in range(len(folders)):
    count = 0
    for root, dirs, files in os.walk(os.path.join(directory,folders[i])):
        #len(files) 
        for filename in files:
           ## if filename does not end in .db, count it. This way the Thumbs.db file will not be counted
            count = count+1
    print("In the subfolder %s, there are" %folders[i])
    print("%s files" %count)
    
    #Completing the DataFrame 
    results_df.iloc[i+2,:] = [folders[i],count]
    
#%%Export the Results as csv
results_df.to_csv("/Users/ecoadmin/Documents/temp/counting_selected_images.csv", index = False) ##Change where you want to save your results!



"""
len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))]) ##this gives you the amount of files. lengthof name?
"""
