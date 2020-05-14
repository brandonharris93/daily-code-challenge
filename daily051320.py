'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

#I don't believe this is O(N) time, but it should be constant space
def recursive_solve(ls):
    if len(ls) == 0:
        return 0
    elif len(ls) == 1:
        return max(0,ls[0])
    elif len(ls) == 2:
        return max(0,ls[0],ls[1])
    else:
        if ls[0]<0 and ls[1]<0:
            return recursive_solve(ls[2:])
        return max(ls[0]+recursive_solve(ls[2:]), ls[1]+recursive_solve(ls[3:]))