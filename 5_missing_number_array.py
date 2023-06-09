'''
Input:
N = 5
A[] = {1,2,3,5}
Output: 4
'''

n = int(input())
arr = list(map(int, input().split()))
sum = 0
total = (n*(n+1))//2

for i in range(n-1):
    sum = sum+arr[i]

print(total - sum)
