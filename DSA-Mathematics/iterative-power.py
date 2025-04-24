"""
In a realm where numbers hold secrets, a captivating challenge awaits, which is to, Compute Power !!!

Problem Description: We are given two numbers. The task is to compute Power(x,n)  which means x to the power y, using, Iterative Power (Binary Exponentiation)

program to calculate pow(x,n)



Examples : 

Input: x = 2, n = 3
Output: 8     

Input: x = 7, n = 2
Output: 49  



In this video, we solve the problem using, Iterative Power (Binary Exponentiation)

Some important concepts related to this approach:

Every number can be written as the sum of powers of 2
We can traverse through all the bits of a number from LSB to MSB in O(log n) time.
Time Complexity: O(log n)

Auxiliary Space: O(1)
"""

# Naive Appraoch

def power_naive(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result

# Test cases
print(power_naive(2, 3))  # Output: 8
print(power_naive(7, 2))  # Output: 49

# Efficient Approach

def power_efficient(x, n):
    result = 1
    while n > 0:
        # If the least significant bit is 1, multiply result by x
        if n % 2 == 1:
            result *= x
        
        # Square the base
        x *= x
        # Right shift the exponent (divide by 2)
        n //= 2
    
    return result

# Test cases
print(power_efficient(2, 3))  # Output: 8
print(power_efficient(7, 2))  # Output: 49
