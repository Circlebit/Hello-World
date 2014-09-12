# this is just a test
# please ignore this file

# returns n!
def factorial(n):
    if n == 1: # base case
        return 1
    else: # recursive step
        return n * factorial(n-1)

print "5! = " + str(factorial(5)) # should be 120
print ""



s = 'math'
i = 0

for c in s:
    print c.upper() + " =",
    if (ord(c)-96) < 10:
        print " " + str(ord(c)-96)
    else:
        print str(ord(c)-96)
    i += ord(c)-96

print "------"
print "    " + str(i) + " = 'the answer to life, the universe and everything.'"

print ""
