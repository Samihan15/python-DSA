#delete node in linked list

def deleteNode(node):
  if not node:
    return
  if not node.next:
    return
  nd = node.next.data
  nn = node.next.next
  node.data = nd
  node.next = nn