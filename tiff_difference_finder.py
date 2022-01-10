#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 16:53:43 2022

@author: filipivic
"""

print('OME-TIFF ')

from apeer_ometiff_library import io
from matplotlib import pyplot as plt

(img1, metadata) = io.read_ometiff('./Moja_level_sets_segmentacija.tiff')
(img2, metadata) = io.read_ometiff('./Ground_truth_segmentacija_inverted.tiff')

intersection1 = img1 - img2
intersection2 = img2 - img1
union = img1 + img2

resolution = img1.size

img1_pixels = 0
img2_pixels = 0
intersection1_pixels = 0
intersection2_pixels = 0
union_pixels = 0

for arrays1 in img1:
    for arrays2 in arrays1:
        for arrays3 in arrays2:
            for arrays4 in arrays3:
                for pixels in arrays4:
                    if (pixels > 200):
                        img1_pixels = img1_pixels +1

for arrays1 in img2:
    for arrays2 in arrays1:
        for arrays3 in arrays2:
            for arrays4 in arrays3:
                for pixels in arrays4:
                    if (pixels > 200):
                        img2_pixels = img2_pixels +1
                        
for arrays1 in union:
    for arrays2 in arrays1:
        for arrays3 in arrays2:
            for arrays4 in arrays3:
                for pixels in arrays4:
                    if (pixels > 200):
                        union_pixels = union_pixels +1                        
                                                                  
for arrays1 in intersection1:
    for arrays2 in arrays1:
        for arrays3 in arrays2:
            for arrays4 in arrays3:
                for pixels in arrays4:
                    if (pixels > 200):
                        intersection1_pixels = intersection1_pixels +1
                        
for arrays1 in intersection2:
    for arrays2 in arrays1:
        for arrays3 in arrays2:
            for arrays4 in arrays3:
                for pixels in arrays4:
                    if (pixels > 200):
                        intersection2_pixels = intersection2_pixels +1
                        
                        
                        
(img3, metadata) = io.read_ometiff('./Moja_level_sets_segmentacija_inverted.tiff')
(img4, metadata) = io.read_ometiff('./Ground_truth_segmentacija.tiff')

intersection = img3 + img4
intersection_pixels = 0

                        
for arrays1 in intersection:
    for arrays2 in arrays1:
        for arrays3 in arrays2:
            for arrays4 in arrays3:
                for pixels in arrays4:
                    if (pixels < 200):
                        intersection_pixels = intersection_pixels +1
                        
##############################################################################   

for arrays1 in img1:
    for arrays2 in arrays1:
        for arrays3 in arrays2:
            plt.imshow(arrays3, interpolation="nearest")
            plt.show()
            
for arrays1 in img2:
    for arrays2 in arrays1:
        for arrays3 in arrays2:
            plt.imshow(arrays3, interpolation="nearest")
            plt.show()
            
for arrays1 in union:
    for arrays2 in arrays1:
        for arrays3 in arrays2:
            plt.imshow(arrays3, interpolation="nearest")
            plt.show()               
                                 
for arrays1 in intersection1:
    for arrays2 in arrays1:
        for arrays3 in arrays2:
            plt.imshow(arrays3, interpolation="nearest")
            plt.show()
            
for arrays1 in intersection2:
    for arrays2 in arrays1:
        for arrays3 in arrays2:
            plt.imshow(arrays3, interpolation="nearest")
            plt.show()

         
for arrays1 in intersection:
    for arrays2 in arrays1:
        for arrays3 in arrays2:
            plt.imshow(arrays3, interpolation="nearest")
            plt.show()
            
print('\n')
            
if (union_pixels - (intersection1_pixels + intersection2_pixels) == intersection_pixels):
    print("Program uspješno dovršen!")
else:
    print("Error")
                        

print('\n')
