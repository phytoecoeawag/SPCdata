#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 12:00:27 2021

@author: Tommy

Script to copy a random sample from a dataset.

Good for creating random validation sets from data of a whole year
"""

import os
import shutil
import random

#%%

home = input('From which directory? It can be a parent directory')
dest = input('To which directory?')
x = int(input('How many images?'))
#initialize list
homelist = []

#%%
"""
a = ['hello','world','beer','gin','scotch',3,56,12,78,9]
b = random.sample(a,2) #a random sample from a of 2 elements
"""

#make a list of all files. Change approach later, this one may be too slow
for a,b,c in os.walk(home): #c is a list of files for each subfolder
    for i in c:
        if i.endswith('.jpeg'):
            homelist.append(os.path.join(a,i)) #a is the path to the last folder

#take a random sample of x elements
randomlist = random.sample(homelist,x) 

#copy each element to destination
for i in randomlist:
    shutil.copy2(i,dest) #change "copy2" to "move" if you want



