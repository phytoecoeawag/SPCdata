#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:56:43 2020

@author: Tommy

This script is used to copy raw_data folders from Q. You can edit it to copy 
folders in a sistematic way. The camera takes pictures every hour. 
Look at line 27

It also makes a .csv file with the dates of the folders you copied
"""

import os
import shutil
from datetime import datetime
import pandas as pd

#%%
home = "/Volumes/ea-daten/Messdaten/AquaScope_data/raw_data/5p0xMAG"
dest = "/Users/ecoadmin/Documents/Time_Efficiency/raw_data"

#%% for folders every week from raw_data
daily = os.listdir(home)
daily.sort(reverse=True) #the list with all timestamps will be sorted
#every week: 1/hour*24h/d*7d/w = 168 instead of 24 a line below, if you want one every week
daily = daily[0::24] #This excludes the 24th (actually 25th) element
#other examples: [1:50:12] or [0:24]

#%% uncomment to check some dates
dates = []
for i in daily:
    dt_object = datetime.fromtimestamp(int(i))
    dates.append(dt_object)

#%% Copying the entire folder of timestamps from Q
for i in daily:
    path = os.path.join(home, i)
    destpath = os.path.join(dest,i)
    #os.mkdir(destpath)
    if os.path.isdir(destpath):
        print('the path for '+i+' already exists')
    else:
        try: #after copying .tar files from Q:, there was an error showing, and it stopped the code
            shutil.copytree(path,destpath)
        except: #this except and pass continues the loop after the error
            pass
        
#%%
dates_csv = pd.DataFrame(dates)
dates_csv.to_csv(os.path.join(dest,'dates.csv'))

#%% This is the same but copies each element individually, instead of folder.
"""
for i in daily:
    path = os.path.join(home, i)
    destpath = os.path.join(dest,i)
    os.mkdir(destpath)
    #only copy the folder if it has not been preprocessed. i.e. only 
    #the 4 original files
    for j in os.listdir(path):
        #print(os.path.join(home,i,'0000000000_static_html/images'))
        #print(os.path.join(dest,i[:-2]))
        path2 = os.path.join(path,j)
        if os.path.isfile(path2):
        #an error showed up and blocked the copy of the next loop
            try:
                shutil.copy2(path2,destpath)
            except:
                pass
        
"""

        
