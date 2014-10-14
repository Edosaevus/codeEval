import math

#Formula for testing primality sourced from most efficient known algorithm
#You dont need to test even numbers greater than 2 (if it's divisible by another
#even number, then we already know it's divisible by 2
#You never need to check higher than n/2
#You never need to check higher than that numbers square root otherwise
#it just flips the divisor which is redundant (repeats every combination twice)

def is_prime(n):
    if n == 2:
        return True
    if n%2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n%divisor == 0:
            return False
    return True

primeCount = 0
currentNum = 1
primeSum = 0

while primeCount < 1000:
    if is_prime(currentNum):
        primeSum += currentNum
        primeCount += 1
    currentNum += 1
print primeSum
    



