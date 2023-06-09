'''

Input: 
n = 4, arr1[] = [1 3 5 7] 
m = 5, arr2[] = [0 2 6 8 9]
Output: 
arr1[] = [0 1 2 3]
arr2[] = [5 6 7 8 9]

'''
n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

i = n-1
j = 0
while(i>=0 and j < m):
    if (arr1[i] > arr2[j]):
        arr1[i],arr2[j] = arr2[j],arr1[i]
        i -= 1 
        j += 1
    else:
        break

print(arr1.sort())
print(arr2.sort())