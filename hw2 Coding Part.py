__author__ = 'Abhik'

import math
import fractions
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



def coPrime(n):
    result = 1

    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            result = k
            if(k!=1):
                break

    print("coprime is " + str(result))
    return result



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
    factorsList = factors(n)
    p,q = factors(n)
    phiN = (p-1) * (q-1)

    #Commented this since e is taken as input, but added the functionality to calculate coPrimes
    #e = coPrime(phiN)

    d = modinv(e,phiN)
    M = (c ** d) % n
    print("p :" + str(p))
    print("q :" + str(q))
    print("d :" + str(d))
    print("M :" + str(M))



def attack2(e,n,c):

    result = 1

    for m in range (1,n+1):
        #Condition as given in the paper, M^e = C mod n
        if(m ** e == c % n):
            print("coming here")
            result = m
            break
    print("M: " + str(result))

e = int(input("enter the value of e"))
n = int(input("enter the value of n"))
c = int(input("enter the value of cipherText"))

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

'''
    OUTPUT 1:

enter the value of e7
enter the value of n15
enter the value of cipherText4
----------------------------------------------------------------------
ATTACK 1
p :5
q :3
d :7
M :4
time take for attack 1 is 0.000137 seconds
----------------------------------------------------------------------
ATTACK 2
M: 1
time take for attack 2 is 5.794e-05 seconds

'''

'''
    OUTPUT 2:

enter the value of e13
enter the value of n527
enter the value of cipherText289
----------------------------------------------------------------------
ATTACK 1
p :31
q :17
d :37
M :51
time take for attack 1 is 0.008504 seconds
----------------------------------------------------------------------
ATTACK 2
M: 1
time take for attack 2 is 0.00069213 seconds


'''

'''
    CUSTOM OUTPUT:

enter the value of e17
enter the value of n86609
enter the value of cipherText12448
----------------------------------------------------------------------
ATTACK 1
p :337
q :257
d :65777
M :18537
time take for attack 1 is 0.052809 seconds
----------------------------------------------------------------------
ATTACK 2
M: 1
time take for attack 2 is 0.084854 seconds
'''