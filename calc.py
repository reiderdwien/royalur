import math
import time

p = 14
m = 16
n = 12

def calc(p,m,n):
    states = 0
    for p1 in range(0,min(m+n+1,p+1)):
        for p2 in range(0,min(m+n+1,p+1)):
            for j in range(max(0,p1-m), min(n,p1) + 1):
                add_states = (p-p1+1)*(p-p2+1)*math.comb(n, j)*math.comb(m, p1 - j)*math.comb(m+n-(p1-j), p2)
                states = states + add_states
    return states

def considerations(p,m,n,states):
    delta_shared = 0
    if p >= 4:
        for p1 in range(4,min(m+n+1,p+1)):
            delta_shared = delta_shared + 2*(p-p1+1)*math.comb(n+m-4,p1-4)
    delta_turns = 0
    for p1 in range(0,min(m+n+1,p+1)):
        delta_turns = delta_turns + 2*(p-p1+1)*math.comb(n+m,p1)
    return 2*(states) - delta_turns - delta_shared
    # delta_turns already gets rid of the "both victory" scenario, since that is really one state, but the factor of 2 considers it as two states

def tests():
    m = 8
    n = 6
    vals = [248,13112,264304,2606947,14680840,53212388,137913936,280408902,482210816,740777984]
    for p in range(1,11):
        if vals[p-1] != calc(p,m,n):
            print("test case error")
    m = 0
    n = 0
    vals = [4, 9, 16, 25, 36]
    for p in range(1,6):
        if vals[p-1] != calc(p,m,n):
            print("test case error")
    m = 1
    n = 0
    vals = [8, 21, 40, 65, 96]
    for p in range(1,6):
        if vals[p-1] != calc(p,m,n):
            print("test case error")
    m = 0
    n = 1
    vals = [9, 25, 49, 81, 121]
    for p in range(1,6):
        if vals[p-1] != calc(p,m,n):
            print("test case error")

tests()

start = time.time()
print(calc(p,m,n))
end = time.time()
print("The time of execution of above program is :", end-start)

print(considerations(1,8,6,calc(1,8,6)))
