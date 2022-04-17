# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:22 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""
from itertools import combinations

# the first way
def sum_in_array(array, number):

    if array != sorted(array):
        array = sorted(array)

    perm = combinations(array, 2)
    for i in perm:
        if i[0] + i[1] == number:
            return i[0], i[1]
    else:
        print([-1])
           
sum_in_array([1, 7, 8, 2, 7, 2, 1, 5, 7, 9, 8, 5], 7)

# the second way
def sum_in_array(array, number):

    if array != sorted(array):
        array = sorted(array)
        
    a = [(i, j) for i in array for j in array if i < j]
    for i in a:
        if i[0] + i[1] == number:
            return i[0], i[1]
    else:
        print([-1])
         

sum_in_array([1, 7, 8, 2, 7, 2, 1, 5, 7, 9, 8, 5], 7)


