'''
move small element to the head of the linked list and large element to the end of the linked list
'''

# error while compiling on CQ platform
'''
Traceback (most recent call last):
  File "/usercode/file.py3", line 80, in <module>
    head = shiftSmallLarge(head);
  File "/usercode/file.py3", line 71, in shiftSmallLarge
    curr.next = new_node
AttributeError: 'NoneType' object has no attribute 'next'
Traceback (most recent call last):
  File "/usercode/file.py3", line 80, in <module>
    head = shiftSmallLarge(head);
  File "/usercode/file.py3", line 71, in shiftSmallLarge
    curr.next = new_node
AttributeError: 'NoneType' object has no attribute 'next'
Traceback (most recent call last):
  File "/usercode/file.py3", line 80, in <module>
    head = shiftSmallLarge(head);
  File "/usercode/file.py3", line 71, in shiftSmallLarge
    curr.next = new_node
AttributeError: 'NoneType' object has no attribute 'next'
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printList(node):
  while (node != None):
    print(node.data, end=' ')
    node = node.next
    
def insertEnd(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
        return head
    
    last = head
    while (last.next):
        last = last.next
    
    last.next =  new_node
    return head 

def delete(head,x):
    if head is None:
        print('Linked list is empty')
        return
    else:
        if x == head.data:
            head = head.next
            return
        else:
            n = head
            while n.next is not None:
                if x == n.next.data:
                    break
                n = n.next
            if n.next == None:
                print('Element doesnt found')
                return
            else:
                n.next = n.next.next

def shiftSmallLarge(head):
    small = head

    curr = head
    while curr is not None:
        if small.data > curr.data:
            small = curr
        curr = curr.next
    
    minEle = small.data

    if minEle == head.data:
        pass
    else:
        delete(head,minEle)

        new_node = Node(minEle)
        new_node.next = head
        head = new_node

    large = head
    curr = head

    while curr is not None:
        if large.data < curr.data:
            large = curr
        curr = curr.next
    
    delete(head,large.data)

    new_node = Node(large.data)
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = new_node

    return head
    

if __name__ == "__main__":
  T = int(input().strip())
  for i in range(T):
    N = int(input().strip())
    head = None
    for j in range(N):
      head = insertEnd(head,int(input().strip()))
    head = shiftSmallLarge(head)
    printList(head)
    print()