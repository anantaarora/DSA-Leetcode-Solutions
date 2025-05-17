class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None



node1 = Node(5)
node2 = Node(76)
node3 = Node(32)
node4 = Node(90)


node1.next = node2
node2.next = node3
node3.next = node4


print(node1)
print(node1.val)
print(node1.next)
print(node1.next.val)
print(node1.next.next.next.val)



class Singly_Linked_List:
    def __init__(self) -> None:
        self.head = None



node1 = Node(5)
node2 = Node(76)
node3 = Node(32)
node4 = Node(90)

sll = Singly_Linked_List()
sll.head = node1

# below both commands will give same output
print(sll.head)
print(node1)

# below both commands will give same output
sll.head.next = node2
node1.next = node2


# Link nodes
node2.next = node3
node3.next = node4

print(sll.head.val)
print(sll.head.next.next.next.val)
print(node1.next.next.next.val)




