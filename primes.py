# Determine if a number is prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(is_prime(1693))
print(is_prime(15))

# Return list of the first 'n' prime numbers
def first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

print(first_n_primes(32))
print(first_n_primes(100))
# /***********************************************************************
#  Using `firstNPrimes`, write a function `sumOfNPrimes(n)` that returns
# the sum of the first `n` prime numbers.
# Examples:
# sumOfNPrimes(0); // => 0
# sumOfNPrimes(1); // => 2
# sumOfNPrimes(4); // => 17
# ***********************************************************************/

# function sumOfNPrimes(n) {
#   let sum = 0;
#   let primes = firstNPrimes(n);

#   for (let i = 0;  i < primes.length; i += 1) {
#       sum += primes[i];
#   }

#   return sum;
# }
