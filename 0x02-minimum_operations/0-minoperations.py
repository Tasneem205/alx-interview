#!/usr/bin/python3
"""function of this problem"""


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generateNextPrime(x):
    """take a number and get the next prime number from it"""
    next_num = x + 1
    while not is_prime(next_num):
        next_num += 1
    return next_num


def primeFactorization(n):
    """generate the prime factorization list"""
    factors = []
    prime = 2
    while n > 1:
        if n % prime == 0:
            factors.append(prime)
            n //= prime
        else:
            prime = generateNextPrime(prime)
    return factors


def minOperations(n):
    """define min copy and paste operations needed"""
    factors = primeFactorization(n)
    return sum(factors)
