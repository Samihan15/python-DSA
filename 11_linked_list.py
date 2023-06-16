class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

'''
node1 = Node(10)
[10,None]
'''

class LinkedList:

    def __init__(self):
        self.head = None

    def printLL(self):
        if self.head == None:
            print('Linked List is empty')
        else:
            while self.head:
                print(self.head.data,end="->")
                self.head = self.head.next

    def add_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def add_after(self,data,x):
        
        if self.head is None:
            print('Linked list is empty')
        else:
            while self.head is not None:
                if x == self.head.data:
                    break
                self.head = self.head.next
            if self.head is None:
                print("X is not found")
            else:
                new_node = Node(data)
                new_node.next = self.head.next
                self.head.next = new_node

    def add_before(self,data,x):
        if self.head is None:
            print('Linked List is empty')
            return
        if self.head == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                if n.next.data == x:
                    break
                n = n.next
            if n.next is None:
                print('node is not found')
            else:
                new_node = Node(data)
                new_node.next = n.next
                n.next = new_node

    def delete(self,x):
        if self.head is None:
            print('Linked list is empty')
            return
        else:
            if x == self.head.data:
                self.head = self.head.next
                return
            else:
                n = self.head
                while n.next is not None:
                    if x == n.next.data:
                        break
                    n = n.next
                if n.next == None:
                    print('Element doesnt found')
                    return
                else:
                    n.next = n.next.next
                    

ll1 = LinkedList()
ll1.add_begin(10)
ll1.add_begin(20)
ll1.add_after(2000,20)
ll1.add_begin(30)
ll1.add_before(33,20)
ll1.add_end(40)
ll1.printLL()