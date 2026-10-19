from math import sqrt
a = [12,15,20]
b = dict((i,[]) for i in a)
def is_prime(x):
    for i in range (2,int(sqrt(x))+1):
        if x % i == 0:
            return False
    return x >1
c = []
for i in a:
    n = i
    for j in range(2,i):
        while n %j == 0 and is_prime(j):
            c.append(j)
            b[i].append(j)
            n//=j
freq={}
for x in c:
    freq[x] = freq.get(x,0) + 1
print(b)
print (c)
print(freq)
print(max(freq,key=freq.get))
