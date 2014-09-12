# this is just a test
# please ignore this file

# returns n!
def factorial(n):
    if n == 1: # base case
        return 1
    else: # recursive step
        return n * factorial(n-1)

print factorial(5) # should be 120