#!/bin/python3

import math
import random
import re

def groupSort(arr):
    frequencyDict = dict()
    for element in arr:
        if element in frequencyDict:
            frequencyDict[element] += 1
        else:
            frequencyDict[element] = 1
    
    return sorted(frequencyDict.items(), key=lambda x: (-x[1], x[0]))
if __name__ == '__main__':
    arr = [3, 3, 1, 2, 1]
    results = groupSort(arr)
    for result in results:
        print(result[0], result[1])
