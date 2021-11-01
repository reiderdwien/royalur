import math

p = 10
m = 8
n = 6
states = 0
for p1 in range (0,p+1):
    for p2 in range (0,p+1):
        for j in range (0, min(n,p1) + 1):
            add_states = (p-p1+1)*(p-p2+1)*math.comb(n, j)*math.comb(m, p1 - j)*math.comb(m+n-(p1-j), p2)
            states = states + add_states
print(states)