# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:51 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""
import re

def lucky(sequence):
    result = re.findall(r'[56|65]{2,}', sequence)
    if not result:
        return 0
    l = []
    for i in result:
        if re.search('^[5]*$', i) or re.search('^[6]*$', i):
            return 0
        else:
            l.append(i)
    return max(l)
            

lucky('4556432455665334')

