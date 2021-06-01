#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:08:20 2020

@author: ecoadmin

Adjust to untar all and not only 0000000000.tar but also 0000006000.tar
for example.
"""
import os
import tarfile

#%%
folder = input("directory?")#"/Users/ecoadmin/Documents/Asterionella_SPCs"
files = os.listdir(folder)
for i in files:
    if not i.startswith('.DS'): 
        if os.path.exists(os.path.join(folder,i,"0000000000.tar")):
            file = os.path.join(folder,i,"0000000000.tar")
            trfile = tarfile.open(file)
            trfile.extractall(os.path.join(folder,i))
    
    
