
# Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P
# where P > 1 and A > 0. A and P both should be integers.

# Example

# Input : 4
# Output : True
# as 2^2 = 4.


# Method to find if input A can be represented as A = i^j (where j > 1)
def isPower(A):
    # If input number is 1, then 1^1 is the answer, hence return True
    if (A == 1):
        return True
    # Starting base i at 2 (because we will never move if base is 1 as 1^n will always be 1)
    i = 2
    # We only need to check base until square root of A, because a base thats greater than sq root of A will always
    # give a number thats greater than A
    # E.g. A = 25, sq rt(A) = 5, so we need to check bases (i) from 2 to 5 (inclusive), any value greater, eg. 6 will
    # have values greater than 25 for any powers greater than 1 (6^2 = 36 which is greater than 25)
    # Because sq root of A might lead to floating point, we consider i^2 <= A
    while (i * i <= A):
        j = 2
        # Check all powers of i, until i^j becomes greater than A
        while (pow(i, j) <= A):
            if (pow(i, j) == A):
                print(i,j)
                return True
            j += 1
        i += 1

    return False

print(isPower(32))