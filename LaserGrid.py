#!/bin/python3

import math
import random
import re

def TotalCost(rows, cols, initR, initC, finalR, finalC, costRows, costCols):
    TotalCostVal = 0

    if initR != finalR:
        if initR < finalR:
            for i in range(initR, finalR):
                TotalCostVal += costRows[i]
        else:
            for i in range(finalR, initR):
                TotalCostVal += costRows[i]
    
    if initC != finalC:
        if initC < finalC:
            for i in range(initC, finalC):
                TotalCostVal += costCols[i]
        else:
            for i in range(finalC, initC):
                TotalCostVal += costCols[i]
    return TotalCostVal
    

if __name__ == '__main__':

    #TotalCostVal = TotalCost(4, 4, 1, 0, 2, 3, [1, 2, 3], [4, 5, 6])
    TotalCostVal = TotalCost(4, 4, 2, 3, 1, 0, [1, 2, 3], [4, 5, 6])
    print(TotalCostVal)
