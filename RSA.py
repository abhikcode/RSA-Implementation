__author__ = 'Abhik'

import math
import time

def powermod(m,e,n):
    return m ** e % n


def is_square(n):
    return math.sqrt(n).is_integer()

#Factorized n = pq using Fermat factoring algorithm
def factors(number):
    k = math.ceil(math.sqrt(number))
    count = 0
    while(not is_square(((k+count) **2) - number)):
        count +=1

    rhs = int(math.sqrt(((k+count) **2) - number))
    p =  (k + count) + rhs
    q = (k + count) - rhs

    return (p,q)


#Source for calculating d i.e Modular multiplicative inverse : Sources: Stackoverflow, wiki and self
def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m


def attack1(e,n,c):
    p,q = factors(n)
    phiN = (p-1) * (q-1)

    d = modinv(e,phiN)
    M = (c ** d) % n
    print("p :" + str(p))
    print("q :" + str(q))
    print("d :" + str(d))
    print("M :" + str(M))


def attack2(e,n,c):

    result = 1

    for m in range(1, n+1):
        # FIX: use pow(m, e, n) so both sides are evaluated mod n
        if pow(m, e, n) == c % n:
            result = m
            break
    print("M: " + str(result))


e = int(input("enter the value of e: "))
n = int(input("enter the value of n: "))
c = int(input("enter the value of cipherText: "))

print("----------------------------------------------------------------------")

print("ATTACK 1")
start = time.time()
attack1(e,n,c)
stop = time.time()
print("time take for attack 1 is " + str(round(stop - start, 6)) + " seconds")

print("----------------------------------------------------------------------")

print("ATTACK 2")
begin = time.time()
attack2(e,n,c)
end = time.time()
print("time take for attack 2 is " + str(round(end - begin, 8)) + " seconds")
