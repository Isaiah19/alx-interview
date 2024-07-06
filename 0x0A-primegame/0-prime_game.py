#!/usr/bin/python3
"""Module defining isWinner function."""

def isWinner(x, nums):
    """Function to get who has won in prime game"""
    def sieve(n):
        """ Helper function to use Sieve of Eratosthenes to find all primes up to n. """
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n + 1, i):
                    is_prime[j] = False
        return [i for i in range(n + 1) if is_prime[i]]
    
    mariaWinsCount = 0
    benWinsCount = 0

    max_num = max(nums)
    primes = sieve(max_num)

    for num in nums:
        roundsSet = list(range(1, num + 1))
        primesSet = [p for p in primes if p <= num]

        if not primesSet:
            benWinsCount += 1
            continue

        isMariaTurn = True

        while True:
            if not primesSet:
                if isMariaTurn:
                    benWinsCount += 1
                else:
                    mariaWinsCount += 1
                break

            smallestPrime = primesSet.pop(0)
            roundsSet.remove(smallestPrime)
            roundsSet = [x for x in roundsSet if x % smallestPrime != 0]
            primesSet = [x for x in primesSet if x % smallestPrime != 0]

            isMariaTurn = not isMariaTurn

    if mariaWinsCount > benWinsCount:
        return "Maria"
    if mariaWinsCount < benWinsCount:
        return "Ben"
    return None

def is_prime(n):
    """Returns True if n is prime, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    """Returns a list of prime numbers between start and end (inclusive)."""
    primes = [n for n in range(start, end+1) if is_prime(n)]
    return primes

