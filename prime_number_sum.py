# Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.
# NOTE A solution will always exist. read Goldbach’s conjecture
# Example:
# Input : 4
# Output: 2 + 2 = 4

# If there are more than one solutions possible, return the lexicographically smaller solution.
# If [a, b] is one solution with a <= b,
# and [c,d] is another solution with c <= d, then
# [a, b] < [c, d] iff a < c OR a==c AND b < d.


# Method to check if a number is prime
# Note that we only need to check numbers from 2 until square root of "num"
# But since square root of num will be a floating point number, we flip the conditional as i*i <= num
def is_prime(num):
    i = 2
    # Only need to check until sq root of num
    while (i * i <= num):
        if (num % i == 0):
            return False
        i += 1
    return True


# Method to find the prime numbers that sum up to the given number
def primesum(A):
    # Only need to check till A/2 because the complement is already checked in the first half of the range
    # e.g. if number is 25, then (2 + 23) == (23 + 2), i.e you've already check out 23 once
    for i in range(2, A // 2 + 1):
        if (is_prime(i) and is_prime(A - i)):
            return (i, A - i)

# Main
print(primesum(9))
