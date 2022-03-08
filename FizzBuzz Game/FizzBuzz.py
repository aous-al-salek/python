# The is a script that will play FizzBuzz.
# FizzBuzz is a game where two people count up in turn from 1 to 100
# and when it is a multiple of 3 the person counting says Fizz, 
# when it is a multiple of 5 the person says Buzz 
# and when it is a multiple of both 3 and 5 the person says FizzBuzz.
# https://en.wikipedia.org/wiki/Fizz_buzz
# The idea was taken from: https://youtu.be/QPZ0pIK_wsc

# This sciprt includes two different solutions.

#####<<<<<Solution 1>>>>>#####
N = []
for n in range(1,101) : 
    N.append(n)
N3 = []
for n in N :
    if n < 35 :
        N3.append(n*3)
N5 = []
for n in N :
    if n < 21 :
        N5.append(n*5)

for n in N :
    if (n in N3 and n in N5) :
        print(n, "FizzBuzz")
        continue
    elif n in N3 :
        print(n, "Fizz")
    elif n in N5 :
        print(n, "Buzz")

#####<<<<<Solution 2>>>>>#####
for n in range(1,101) :
    if (n % 3 == 0 and n % 5 == 0) :
        print(n, "FizzBuzz")
        continue
    elif n % 3 == 0 :
        print(n, "Fizz")
    elif n % 5 == 0 :
        print(n, "Buzz")
