# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 11:26:23 2020

@author: Tommy Hardeman

Deleting the raw_color and binary files to make a sample for the classifier of only 
"useful" .jpegs

Make a directory with only the subfolders that were already SPC-converted
This script will look for the "_static_html" folder

TODOS: Adjust to do all folders and not only 0000000000.tar but also 
0000006000.tar, for example.
"""

import os
import shutil
#%% Deleting and copying resulting files to plankifier testing directory

#In this directory are the folders with unix timestamp name
#home = "/Users/ecoadmin/Documents/SPC_centrales" 
home = input("directory?")

#This is if you wish to copy the files to somewhere else:
destination = ""

sub_temp = os.listdir(home)
subfolders = os.listdir(home) # get a list of the subfolders
paths = []

for i in subfolders:
    path0 = os.path.join(home,i) #"../1573552801"
    if os.path.isdir(path0): #to not iterate over the hidden .DS file
        for static in os.listdir(path0):
            if static.endswith('_html'):
                #"../1573552801/_static_html/images"
                path1 = os.path.join(path0,static+'/images')
                for a in os.listdir(path1):
                    #path2 = "../1573552801/_static_html/images/02001"
                    path2 = os.path.join(path1,a)
                    if os.path.isdir(path2):
                        temp = os.listdir(path2) 
                        for name in temp:
                            if name.endswith('binary.png') or name.endswith('rawcolor.jpeg'):
                                #path3 = "../1573552801/_static_html/images/06001/SPC-[..]_rawcolor.jpeg"
                                path3 = os.path.join(path2,name)
                                os.remove(path3) #delete that file
                        #copy the files to the destination folder
                        #shutil.copytree(path2,destination+'/test_validation/'+'images/'+i)
               

                
    