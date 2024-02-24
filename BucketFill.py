#!/bin/python3

import math
import random
import re

isVisited = []

def IsInsideBoundary(x, y, h, w):
    if x < 0 or y < 0 or x >= h or y >= w:
        return False
    else:
        return True
def AdjacencyTraversal(picture, x, y, h, w):
    global isVisited
    isVisited[x][y] = 1
    if IsInsideBoundary(x - 1, y, h, w):
        if not isVisited[x - 1][y]:
            if picture[x - 1][y] == picture[x][y]:
                AdjacencyTraversal(picture, x - 1, y, h, w)
    if IsInsideBoundary(x + 1, y, h, w):
        if not isVisited[x + 1][y]:
            if picture[x + 1][y] == picture[x][y]:
                AdjacencyTraversal(picture, x + 1, y, h, w)
    if IsInsideBoundary(x, y - 1, h, w):
        if not isVisited[x][y - 1]:
            if picture[x][y - 1] == picture[x][y]:
                AdjacencyTraversal(picture, x, y - 1, h, w)
    if IsInsideBoundary(x, y + 1, h, w):
        if not isVisited[x][y + 1]:
            if picture[x][y + 1] == picture[x][y]:
                AdjacencyTraversal(picture, x, y + 1, h, w)

def StrokesRequired(picture, h):
    stroke = 0
    w = len(picture[0])
    global isVisited
    isVisited = [[0 for x in range(w)] for y in range(h)]
    for x in range(h):
        for y in range(w):
            if not isVisited[x][y]:
                stroke += 1
                AdjacencyTraversal(picture, x, y, h, w)
    return stroke

if __name__ == '__main__':

    picture = ["aaaba", "ababa", "aaaca"]
    print(StrokesRequired(picture, 3))
