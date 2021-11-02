import math

p = 70
m = 80
n = 60

def calc(p,m,n):
    states = 0
    for p1 in range(0,min(m+n+1,p+1)):
        for p2 in range(0,min(m+n+1,p+1)):
            for j in range(max(0,p1-m), min(n,p1) + 1):
                add_states = (p-p1+1)*(p-p2+1)*math.comb(n, j)*math.comb(m, p1 - j)*math.comb(m+n-(p1-j), p2)
                states = states + add_states
    print(states)
    return states

def tests():
    m = 8
    n = 6
    for p in range (1,11):
        calc(p,m,n)

tests()

calc(p,m,n)
