# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

# pseudocode

# create a function checking whether the value is less tha or greater than 1000
def product_or_sum (first_integer, second_integer):

# multiply the two integer
    product = first_integer * second_integer

# add the two integer
    sum = first_integer + second_integer

# print the product if less than or equal to 1000
    if product <= 1000:
        print ("The value of the number is", product)

# print the sum if greater than 1000
    else:
        print ("The value of the number is", sum)

# first example
problem_one = product_or_sum (90, 80)

# second example
problem_two = product_or_sum (30, 10)