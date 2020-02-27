from builtins import input, min
import math
import bs4
def isPrime(x):
    for i in range(2, x):
        if x % i==0:
            print(x," is not prime")
            return;
    print(x,"isprime")


a = int(input());
isPrime(a)
