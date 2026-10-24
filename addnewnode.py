# create linked list
class Node:
    def __init__(self, val):
       self.val = val
       self.next =None 

class SinglyLinkedlist:
    def __init__(self) -> None: 
      self.head = None


    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
              current= current.next
            current.next = new_node 

    #Traverse and print the node values            

    def display(self):
        current = self.head
        while current is not None:
            print(current.val, end=" -> ")
            current =current.next 

    # insert node at specific position
    def insert_position(self, val, position):
        new_node = Node(val)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head

        for i in range(position -1):
            if current is None:
                print("position is invalid")
                return
            current = current.next
            if current is None:
                print("position is invalid")
                return
            new_node.next = current.next
            current.next = new_node 

    # Find and print the middle node
    def find_middle(self):
        if self.head is None:
            print("List is empty")
            return

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        print("middle node:", slow.val) 

    # Delete the node from the list
    def delete(self, val):
        if self.head is None:
            print("list is empty")
            return
        if self.head.val == val:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
                return
            current = current.next
        print("values is not found")

    # reverse the linked list
    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    #Calculate the sum of every two consecutive node values. 

    def sum_consecutive(self):
        current = self.head

        while current is not None and current.next is not None:
            total = current.val + current.next.val
            print(current.val, "+", current.next.val, "=", total)
            current = current.next            

        print("None") 
my_list=SinglyLinkedlist()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.display()

my_list.insert_position(15,2)
print(" after inserting at position 2:")
my_list.display()

my_list.find_middle()

my_list.delete(20)
print("After deleting 20:")
my_list.display()

my_list.reverse()
print("Reversed list:")
my_list.display()

my_list.sum_consecutive()