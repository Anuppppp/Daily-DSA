"""
Problem: Print Numbers in Reverse using Recursion

Description:
Write a recursive function that takes a positive integer N
and prints numbers from N to 1 using recursion.

You are NOT allowed to use loops. The goal is to understand
how recursive calls can "go deep" and then print while returning.

Example:
Input: 5
Output:
5
4
3
2
1

Explanation:
The function should first call itself with (N-1) until it reaches 1,
then print the values in the reverse order of how the calls were made.

Constraints:
- 1 <= N <= 1000
"""

def print_reverse(n):
    """
    Recursively prints numbers from n down to 1.

    Parameters:
    n (int): The starting positive integer
    """
    if n == 0:
        return
    print(n)
    print_reverse(n-1)


# Example usage
if __name__ == "__main__":
    print_reverse(5)
