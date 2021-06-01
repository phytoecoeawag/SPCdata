#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 15:22:53 2021

@author: Tommy

This is a script to check from which dates are your pictures in a folder
Does not check for subfolders. Yet. It saves the results as a .csv file
It also plots how many images come from which day
"""

import os
from datetime import datetime 
import pandas as pd
from collections import Counter
import time
import matplotlib.pyplot as plt

home = input('directory?')

names = os.listdir(home)
for j in names:
    if not (j.endswith('.jpg') or j.endswith('.jpeg')):
        names.remove(j) #remove hiddenfiles from list

#initialize lists
timestamps = []
dates = []
days = []

for i in names: #the characters 15 until 21 tell you the date
    times = i[15:22]+'000' #only take characters of the day SPC
                        #complete to full datetime length with '000'
    timestamp = int(times) #make it an integer            
    timestamps.append(timestamp) #append it to the list
    dt_object = datetime.fromtimestamp(timestamp) #convert it to date object 
    date = dt_object.strftime("%d/%m/%Y, %H:%M:%S") #convert it to string
    day = dt_object.strftime("%d/%m/%Y") #just get it to day resolution
    dates.append(date) #append it to list
    days.append(day)

"""
#%%list all dates and the timestamps
#dummy = {'timestamp':timestamps,'date':dates} #dictionary with both
dummy = {'timestamp':timestamps,'date':days} #dictionary with both
result = pd.DataFrame(dummy) #make it a dataframe
result = result.set_index('timestamp')
result = result.sort_values(by=['timestamp'])
#result.to_csv(os.path.join(home,'dates.csv')) #turn it to .csv
"""
#%% Count the timestamps and make a list

counter = dict(Counter(days)) #Counter counts how many times an element is present 
results_counter = pd.DataFrame(counter, index = [0]).T
daystimestamps = []

for j in results_counter.index:
    daytimestamp = time.mktime(datetime.strptime(j,"%d/%m/%Y").timetuple())
    daystimestamps.append(daytimestamp)
results_counter['Timestamp']=daystimestamps #make the column of timestamps in dataframe
results_counter = results_counter.reset_index()
#results_counter = results_counter.set_index('Timestamp')
results_counter = results_counter.sort_values(by=['Timestamp'])
results_counter.columns = ['Date','Count','Timestamp']
results_counter.to_csv(os.path.join(home,'dates_count.csv'))

"""
#%% Plot timestamps, just to check. comment or delete the """

results_counter.plot(x='Timestamp',y='Count')
"""
#%% Plot dates

x = [] #x-axis convert strings to datetime
for k in results_counter['Date']:
    x.append(datetime.strptime(k, "%d/%m/%Y"))
y = results_counter['Count'] 

fig, ax = plt.subplots()
plt.plot_date(x,y)
ax.xaxis.set_tick_params(rotation=30, labelsize=10)




