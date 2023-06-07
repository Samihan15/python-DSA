n = int(input("Enter number \n"))


'''
*
* * 
* * *
* * * *
* * * * *
'''
for i in range(n):
    for j in range(i):
        print("* ",end="")
    print("\n")



'''
* * * * *
* * * *
* * *
* *
*
'''

for i in range(n):
    for j in range(n-i):
        print("* ",end = "")
    print("\n")


'''
      *
    * *
  * * *
* * * *
'''

for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()


