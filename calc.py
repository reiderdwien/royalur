import math

p = 70
m = 80
n = 60

def calc(p,m,n):
    states = 0
    for p1 in range(0,min(m+n+1, p+1)):
        for p2 in range(0,min(m+n+1, p+1)):
            for j in range(0, p1 + 1):
                add_states = (p-p1+1)*(p-p2+1)*math.comb(n, j)*math.comb(m, p1 - j)*math.comb(m+n-(p1-j), p2)
                states = states + add_states
    return states

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

print(calc(p,m,n))
