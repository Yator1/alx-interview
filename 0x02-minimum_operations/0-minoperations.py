#!/usr/bin/python3
"""
Method that calculates the fewest number of operations needed to result
in exactly n H characters in the file.
"""


def minOperations(n):
    """
    A method for calculating the operations
    """
    ops = 0 # keeping track of operations
    factor = 2 # checking from factor 2

    # looping until n is one
    while n > 1:
        # dividing the n by the current factor if divisible proceed to loop
        while n % factor == 0:
            # adding current factor to operation
            ops += factor
            # divide the n with the ops to get a new n
            n //= ops
        
        # if not divisible add factor by 1
        factor += 1
    
    # return total ops required
    return ops
