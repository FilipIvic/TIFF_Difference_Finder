#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 13:46:14 2022

runfile('tiff_difference_finder.py', args='./Moja_level_sets_segmentacija.tiff ./Ground_truth_segmentacija_inverted.tiff ./Moja_level_sets_segmentacija_inverted.tiff ./Ground_truth_segmentacija.tiff')

@author: filipivic and irenadragicevic
"""

print('OME-TIFF ')

from apeer_ometiff_library import io
from matplotlib import pyplot as plt   

if __name__ == '__main__':
        
    (img1, metadata) = io.read_ometiff("./Moja_level_sets_segmentacija.tiff")
    (img2, metadata) = io.read_ometiff("./Ground_truth_segmentacija_inverted.tiff")
    
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
                            
                            
                            
    (img3, metadata) = io.read_ometiff("./Moja_level_sets_segmentacija_inverted.tiff")
    (img4, metadata) = io.read_ometiff("./Ground_truth_segmentacija.tiff")
    
    intersection = img3 + img4
    intersection_pixels = 0
    
                            
    for arrays1 in intersection:
        for arrays2 in arrays1:
            for arrays3 in arrays2:
                for arrays4 in arrays3:
                    for pixels in arrays4:
                        if (pixels < 200):
                            intersection_pixels = intersection_pixels +1
                            
    ###########################-Ispis Grafova-################################   
    
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
        print("\n")
        print("Rezolucija slike je: " + str(resolution) + " pixela")
        print("Površina segmentiranog tijela slike iznosi: " + str(img1_pixels) + " pixela")
        print("Površina segmentiranog tijela slike iznosi: " + str(img2_pixels) + " pixela")
        print("\n")
        print("Unija površina segmeniranih tijela iznosi: " + str(union_pixels) + " pixela")
        print("Presjek površina segmeniranih tijela iznosi: " + str(intersection_pixels) + " pixela")
        print("\n")
        print("Površina ostatka presjeka tijela sa slike sa tijelom sa slike iznosi: " + str(intersection1_pixels) + " pixela")
        print("Površina ostatka presjeka tijela sa slike sa tijelom sa slike iznosi: " + str(intersection2_pixels) + " pixela")
        
    else:
        print("ERORR!!!")
            
        
    #else:
       # print("Krivo unesena imena slika!!!")              
    
    print('\n')
