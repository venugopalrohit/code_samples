# Google interview
# Question: https://www.careercup.com/question?id=5657872336683008
# Generate a even random number, with non-repeating adjacent digits

import random

# Remember, these are sets and not lists
all_digits = {0,1,2,3,4,5,6,7,8,9}
even_digits = {0,2,4,6,8}


def rand_generator(num_of_digits):
    digit_array = []

    # Highest power digit has to initialized first, because it has no restrictions on matching, except that it shouldn't
    # be 0
    digit_array.append(random.choice(list(all_digits - {0})))

    for i in range(1, num_of_digits - 1):
        digit_array.append(random.choice(list(all_digits - {digit_array[i-1]})))

    # Last digit is even, and has not be different from the second-list digit
    digit_array.append(random.choice(list(even_digits - {digit_array[num_of_digits - 2]})))

    print(digit_array)

    # Now that we have the array of random digits, we create a number out of them
    my_pow = 1
    final_num = 0
    for i in range(num_of_digits - 1, -1, -1):
        final_num += (digit_array[i] * my_pow)
        my_pow *= 10

    print(final_num)



rand_generator(8)

# a = random.choice(list(all_digits - {0}))
# print(a)
# b = list(all_digits - {a})
# print(b)

