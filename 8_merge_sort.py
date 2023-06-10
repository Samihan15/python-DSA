'''
MergeSort algorithm
'''

# 2 1 6 5 4

def mergeSort(arr):
    if(len(arr)>1):             # divide function 
        mid = len(arr)//2       # mid element of array
        left_arr = arr[:mid]    # 2 1
        right_arr = arr[mid:]   # 6 5 4
        mergeSort(left_arr)
        mergeSort(right_arr)

        i = 0
        j = 0
        k = 0

        while(i<len(left_arr) and j < len(right_arr)):
            if(left_arr[i] < right_arr[j]):
                arr[k] = left_arr[i]
                i+=1
                k+=1
            else:
                arr[k] = right_arr[j]
                j+=1
                k+=1

        while i<len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1
        
        while j<len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1


num = int(input())
arr = [int(input()) for i in range(num)]
mergeSort(arr)
print("sorted list ",arr)