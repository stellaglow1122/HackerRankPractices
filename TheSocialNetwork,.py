#!/bin/python3

import math
import random
import re

def Grouping(counts):
    resultGroups = dict()
    for i in range(len(counts)):
        if counts[i] in resultGroups.keys():
            resultGroups[counts[i]].append(i)
        else:
            tempList = []
            tempList.append(i)
            resultGroups[counts[i]] = tempList
    for count, IDs in resultGroups.items():
        IDs.sort()
        i = 0
        while i < len(IDs):
            group = str(IDs[i])
            for j in range(1, count):
                group += ' ' + str(IDs[i + j])
            print(group)
            i += count


if __name__ == '__main__':

    counts = [3, 3, 3, 3, 3, 1, 3]
    counts = [2, 2, 2, 2]
    Grouping(counts)
