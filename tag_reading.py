#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 17:09:56 2021

@author: Tommy

Tests done with temp/test5

Reading Tags in Mac and organize them to later copy to Q or any other destination.
To make validation or training sets from images in different folders but with same tag.
"""

import os
import mac_tag
import pandas as pd
import shutil

#%% Read directories

#home = input('home directory?')
home = '/Users/ecoadmin/Documents/temp/test5/home'
#dest = input('destination?')
dest = '/Users/ecoadmin/Documents/temp/test5/dest'

pathlist = []
taglist = []
copied_to = []

for a,b,c in os.walk(home):
    print(a,b,c)
    #path_1 = os.path.join(a,c)
    for i in c:
        filepath = os.path.join(a,i)
        if i.startswith('.DS') or i.endswith('Thumbs.db'):
            continue #don't read or copy these files, continue to next iteration
        if os.path.isfile(filepath):
            tags_dict = mac_tag.get(filepath) #this gives you a dictionary object
            class_tag = tags_dict[filepath][0][2:]#Calling tags_dict[filepath]
            #spits out all tags as a list. The first element is the class
            #remove the "1_" part of the tag
            pathlist.append(filepath)
            taglist.append(class_tag)
            #now paste this file to the destination in a folder with the 
            #tag name. This can also be in Q!
            dest_folder_path = os.path.join(dest,class_tag)
            
            if not os.path.isdir(dest_folder_path) :
                os.mkdir(dest_folder_path)#if the folder doesn't exist, make
            
            shutil.copy2(filepath,dest_folder_path)#copy the file from home
            copied_to.append(os.path.join(dest_folder_path,i))

taglist_df = pd.DataFrame([pathlist,taglist,copied_to]).T
taglist_df.columns=['Home Path','Tag','Dest Path']

            
