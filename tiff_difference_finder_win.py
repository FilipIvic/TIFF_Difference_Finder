#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 16:53:43 2022
runfile('tiff_difference_finder_win.py', args='Moja_level_sets_segmentacija.tif Ground_truth_segmentacija.tif')
runfile('tiff_difference_finder_win.py', args='Moja_level_sets_segmentacija.tif Moja_level_sets_segmentacija.tif')
@author: filipivic and irenadragicevic
"""

from apeer_ometiff_library import io
from matplotlib import pyplot as plt
import sys
import glob
import os

#def tiff_difference_finder(img1_path, img2_path, img3_path, img4_path):
def tiff_difference_finder(img1_path, img2_path):
    (img1, metadata) = io.read_ometiff("./" + img1_path)
    (img2, metadata) = io.read_ometiff("./" + img2_path)
    
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
    
    print('\n')
    print("Program uspješno dovršen!")
    print("\n")
    
    print("Rezolucija slike je: " + str(resolution) + " pixela")
    print("Površina segmentiranog tijela slike " + img1_path[:-5] + " iznosi: " + str(img1_pixels) + " pixela")
    print("Površina segmentiranog tijela slike " + img2_path[:-5] + " iznosi: " + str(img2_pixels) + " pixela")
    print("\n")
    
    print("Unija površina segmeniranih tijela iznosi: " + str(union_pixels) + " pixela")
    print("Presjek površina segmeniranih tijela iznosi: " + str(union_pixels - (intersection1_pixels + intersection2_pixels)) + " pixela")
    print("\n")
    
    print("Površina ostatka presjeka tijela sa slike " + img1_path[:-5] + " sa tijelom sa slike " + img2_path[:-5] + " iznosi: " + str(intersection1_pixels) + " pixela")
    print("Površina ostatka presjeka tijela sa slike " + img2_path[:-5] + " sa tijelom sa slike " + img1_path[:-5] + " iznosi: " + str(intersection2_pixels) + " pixela")
    print("\n")
    
    print("Postotak poklapanja slika: " + str((union_pixels - (intersection1_pixels + intersection2_pixels))/union_pixels * 100) + "%")
        
   
if __name__ == '__main__':
    
    program = sys.argv[0]
    
    img1_path = sys.argv[1]
    img2_path = sys.argv[2]
    
    names = [os.path.basename(name) for name in glob.glob("*")]
    if img1_path and img2_path in names:
        tiff_difference_finder(img1_path, img2_path)
        
    else:
        print("Krivo unesena imena slika!!!")              
    
    print('\n')