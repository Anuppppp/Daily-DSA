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

#  Naive solution

def computing_power(x, n):
    res = 1
    for i in range(n):
        res = res * x
    return res


print(computing_power(2, 3))