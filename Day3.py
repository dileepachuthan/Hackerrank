#Day 3: Intro to Conditional Statements
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input("Number:"))
    for i in range(N):
        if N % 2 != 0:
            print("Weird")
            break
        if N > 20 and N % 2 == 0:
            print("Not Weird")
            break
        if N <6 and N>2 and N %2 == 0:
            print("Not Weird")
            break
        if N <=20 and N>=6 and N %2 == 0:
            print("Weird")
            break
