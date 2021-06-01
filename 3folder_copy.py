# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 11:22:02 2020

@author: Tommy

This script checks if the files in the 'home1' directory also exist in 'home2'
and in 'home3'. IF they DO NOT exist in home2 AND in home3, the files will be
copied from home1 to home3.

"""
home1 = "Q:/Messdaten/AquaScope_data/pictures/selected_pics/0p5x"
home2 = "Q:/Messdaten/AquaScope_data/pictures/annotation_classifier/1_zooplankton_0p5x/training/zooplankton_trainingset_2020.04.28"
home3 = "Q:/Messdaten/AquaScope_data/pictures/library/0p5x"

import os
import shutil


#list of classes to compare
#class_folders = os.listdir(home1)
#if you wish to compare just some selected folders write them as a list
class_folders = ['paradileptus']
#class_folders = ['cyclops', 'ceratium', 'conochilus', 'daphnia', 'dinobryon', 'fragilaria', 'hydra', 'keratella_cochlearis', 'kellikottia', 'keratella_quadrata', 'paradileptus', 'polyarthra', 'synchaeta',  ]

for subf in class_folders:
    folder1 = os.path.join(home1,subf)
    #folder2 had an extra-subdirectory 'training_data' 
    folder2 = os.path.join(home2,subf+"/training_data")
    folder3 = os.path.join(home3,subf)
    all_files1 = []
    all_files2 = []
    all_files3 = []
    
    #Make lists of all the files in the class_folder, also files in subdirectories
    for root, dirs, files in os.walk(folder1):
        #print(root, dirs, files) #to see how os.walk works
        for items in files:
            #sometimes there are unwanted hidden 'Thumbs.db' files
            if not items.endswith('Thumbs.db'):
                all_files1.append(root+"/"+items)
            
    for root, dirs, files in os.walk(folder2):
        for items in files:
            if not items.endswith('Thumbs.db'):
                all_files2.append(root+"/"+items)
    
    for root, dirs, files in os.walk(folder3):
        for items in files:
            if not items.endswith('Thumbs.db'):
                all_files3.append(root+"/"+items)
            
    #If a file (x) from home1 is NOT in home2 and home3, copy it to home3
    for x in all_files1:
        #if the amount of files with name (x) is 0, copy file (x) from folder1 to folder3
        if all_files2.count(x) == 0 and all_files3.count(x) == 0: 
            shutil.copy(x,folder3)

