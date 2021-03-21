#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_hourglass_sum = arr[0][0] + arr[0][1] + arr[0][2] + arr [1][1] + arr[2][0] + arr[2][1] + arr[2][2]
    for r in range(4):
        for c in range(4):
            current_hourglass_sum = 0
            current_hourglass_sum = arr[r][c] + arr[r][c + 1] + arr[r][c + 2] + arr [r + 1][c + 1] + arr[r + 2][c] + arr[r + 2][c + 1] + arr[r + 2][c + 2]
            if current_hourglass_sum > max_hourglass_sum:
                max_hourglass_sum = current_hourglass_sum
    return max_hourglass_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
