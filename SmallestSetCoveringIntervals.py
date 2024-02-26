#!/bin/python3

import math
import random
import re

def interval(first, last):
    intervals = list()
    for i in range(len(first)):
        temp = list()
        temp.append(first[i])
        temp.append(last[i])
        intervals.append(temp)
    intervals.sort(key=lambda x: (x[1], -x[0]))
    res = [intervals[0][1] - 1, intervals[0][1]]  
    for i in range(1, len(first)):
        start = intervals[i][0]
        end = intervals[i][1]
 
        if start > res[-1]:
            res.append(end - 1)
            res.append(end)
        elif start > res[-2]:
            res.append(end)
    return len(res)
        

if __name__ == '__main__':
    first = [3, 2, 0, 4]
    last = [6, 4, 2, 7]
    result = interval(first, last)
    print(result)
