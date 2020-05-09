'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, 
find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative 
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

import numpy as np

def lowest_pos_int(input):
    #this solution actually does not fit the parameters given, as it is supposed to use constant space and linear time
    #this line uses linear space
    indices = np.ones(len(input)+1,dtype=bool)
    for i in input:
        if i > 0 and i <= len(input)+1:
            indices[i-1] = False

    return np.argmax(indices) + 1

def lowest_pos_int_alt(input):
    #this alternative solution should use less space since it modifies the input list in place rather than creating
    #a parallel boolean array
    min = 1
    max = len(input)
    for i in range(max):
        tmp = input[i]
        if min<=tmp and tmp<=max:
            #swap each number within the possible range for its place in sequence
            input[tmp-1], input[i] = tmp, input[tmp-1]
    #if a number is in the array, it has been put in its appropriate place in the sequence
    #therefore if the number in the array doesn't match its (1-based) index number, it is missing
    #the first such number we find is the lowest missing positive integer
    for i in range(max):
        if i+1 != input[i]:
            return i+1
    return max+1

