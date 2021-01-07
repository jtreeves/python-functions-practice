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

print(first_n_primes(10))
print(first_n_primes(20))

# Return sum of the first 'n' prime numbers
def sum_of_n_primes(n):
    sum = 0
    primes = first_n_primes(n)
    for i in range(len(primes)):
        sum += primes[i]
    return sum

print(sum_of_n_primes(3))
print(sum_of_n_primes(10))