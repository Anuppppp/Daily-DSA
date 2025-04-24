"""
In a realm where numbers hold secrets, a captivating challenge awaits, which is to, Compute Power !!!

Problem Description: We are given two numbers. The task is to compute Power(x,n)  which means x to the power y.

program to calculate pow(x,n)



Examples : 

Input: x = 2, n = 3
Output: 8      // 2*2*2

Input: x = 7, n = 2
Output: 49   // 7*7
"""

#  Naive Approach

def computing_power(x, n):
    res = 1
    for i in range(n):
        res = res * x
    return res



# Efficient Approach

def computing_power(x, n):
    if n == 0:
        return 1
    temp = computing_power(x, n//2)
    temp = temp * temp
    if n % 2 == 0:
        return temp
    else:
        return temp * x

print(computing_power(2, 3))