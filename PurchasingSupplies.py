#!/bin/python3

import math
import random
import re

def maximumContainers(scenarios):
    for scenario in scenarios:
        parameter = scenario.split(' ')
        n = int(parameter[0])
        cost = int(parameter[1])
        m = int(parameter[2])
        totalContainer = int(n / cost)
        extraContainer = totalContainer
        while int(extraContainer / m) > 0:
            totalContainer += int(extraContainer / m)
            extraContainer = int(extraContainer / m) + extraContainer % m
        print(totalContainer)

if __name__ == '__main__':
    scenarios = ['10 2 5', '12 4 4', '6 2 2']
    maximumContainers(scenarios)
