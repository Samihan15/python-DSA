'''
INPUT
N = 4 
arr[] = {1,5,3,2}

OUTPUT
2
'''

n = int(input())
arr = list(map(int, input().split()))
count = 0
s = set(arr)

for i in range(n-1):
    for j in range(i+1,n):
        if arr[i] + arr[j] in s:
            count += 1

print(count)