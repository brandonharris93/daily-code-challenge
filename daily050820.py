'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, 
find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative 
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

import numpy as np

def lowest_pos_int(input):
    indices = np.ones(len(input)+1,dtype=bool)
    for i in input:
        if i > 0 and i <= len(input)+1:
            indices[i-1] = False

    return np.argmax(indices) + 1