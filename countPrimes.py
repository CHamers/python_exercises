#Write a function that returns the number of prime numbers that exist up to and including a given number

def countPrimes(num):
    #check for 0 or 1 input
    if num < 2:
        return 0
    #for input greater than 1
    #store our prime numbers
    primes = [2]
    #counter going up to the input number
    x = 3
    #x is going through every number up to the input number
    while x <= num:
        #check if x is prime
        for y in primes:
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
           
    
print(countPrimes(100))