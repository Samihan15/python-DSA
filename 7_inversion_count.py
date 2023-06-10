'''
Input: N = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3 

Input: N = 5
arr[] = {2, 3, 4, 5, 6}
Output: 0

Input: N = 3, arr[] = {10, 10, 10}
Output: 0
'''

n = int(input())
arr = list(map(int, input().split()))
count = 0
for i in range(n):
    for j in range(i+1,n):
        if (arr[i]>arr[j]):
            count += 1

print(count)