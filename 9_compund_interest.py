import math
p,r,t = map(int,input().split())
a = p*(pow(1+r/100,t))

print(round(a,1))