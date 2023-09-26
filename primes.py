"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Number of primes cannot be 0 or negative")

    list = []
    y = 2
    while len(list) < number_of_primes:
        if is_prime(y):
            list.append(y)
        y += 1
    return list
