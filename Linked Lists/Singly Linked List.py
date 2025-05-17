class Node:
    def __init__(self, val) -> None:
        self.val =  val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self,value):
        new_node = Node(value)

        if not self.head:
            self.head =  new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next =  new_node

    def traverse(self):
        if not self.head:
            print("SLL is empty")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()

    def insertAtStart(self, value):
        new_node =  Node(value)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head =  new_node


    def insert(self, value, index):
        new_node =  Node(value)
        if index == 0:
            pass # this we have to do
        else:
            temp = self.head
            count = 0 
            while temp:
                count += 1
                temp = temp.next
                if count == index:
                    break
            new_node.next = temp.next
            temp.next = new_node
            # print(temp.val)


    def deleteHead(self):
        if self.head is None:
            print("Cannot delete anything, SLL is empty")
            return
        self.head = self.head.next

    def deleteByValue(self, value):
        if self.head is None:
            print("Cannot delete anything, SLL is empty")
            return
        temp = self.head

        # condition if we want first element to delete
        if temp.val == value:
            self.head =  self.head.next
        else:
            found = False
            while temp is not None:
                if temp.val  == value:
                    found = True
                    break
                prev = temp
                temp = temp.next

            if found:
                prev.next =  temp.next
            else:
                print("None not found")

    def deletebyIndex(self, index):
        if index < 0:
            raise IndexError("Index cannot be negative")

        # If the list is empty
        if self.head is None:
            raise IndexError("Index out of bounds: the list is empty")

        # If deleting the head node
        if index == 0:
            self.head = self.head.next
            return
        
        # Traverse the list to find the node at the specified index
        temp = self.head
        prev = None
        current_index = 0

        while temp is not None and current_index < index:
            prev = temp
            temp = temp.next
            current_index += 1

        # If the index is out of bounds
        if temp is None:
            raise IndexError("Index out of bounds")

        # Delete the node by adjusting the next pointer of the previous node
        prev.next = temp.next


    def search(self, value) -> bool:
        temp =  self.head
        while temp is not None:
            if temp.val == value:
                return True
            temp = temp.next
        
        print("Value not found")
            



sll = SinglyLinkedList()
sll.append(100)
sll.append(200)
sll.append(500)
sll.append(300)
sll.insertAtStart(50)
sll.traverse()
sll.insert(1000, 3)
sll.traverse()
sll.deleteHead()
sll.traverse()
sll.deleteByValue(300)
sll.traverse()
print(sll.search(100))


