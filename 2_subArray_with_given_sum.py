'''
two inputs
N,S = elements in arrays, sum
A = array
INPUT
5 12
1 2 3 7 5

OUTPUT
2 4
'''

sum = 0
start = 0
flag = 0
n,s = map(int ,input().split())
a = list(map(int, input().split()))
for i in range(n):
    sum = sum + a[i]
    while(sum > s):
        sum = sum - a[start]
        start += 1
    
    if(sum == s):
        flag = 1
        r = str(start + 1) + " "+str(i+1)
        print(r)
        break
        

if(flag == 0):
    print(-1)