"""
In a realm where numbers hold secrets, a captivating challenge awaits, which is to, Find all the Prime Numbers less than or equal to a given Number !!!

Problem Description: Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number.



Example:

Input : n =10
Output: 2 3 5 7

Input : n = 20
Output: 2 3 5 7 11 13 17 19

"""

def sieve_of_eratosthenes(n):
    if n == 0 or n == 1:
        return False
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p*p, n+1, p):
                is_prime[i] = False
        p = p + 1
    primes = [i for i in range(n+1) if is_prime[i]]
    return primes


num = int(input("Enter a number : ", ))
print(sieve_of_eratosthenes(num))


