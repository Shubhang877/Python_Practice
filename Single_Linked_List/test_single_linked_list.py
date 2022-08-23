from single_linked_list import Node,SingleLinkedList


node1=Node(1)
node2=Node(2)
node1.next=node2

ll=SingleLinkedList()
ll.head=node1

newnode=Node(0)
ll.addNodeAtPosition(newnode,0)

newnode=Node(4)
ll.addNodeAtPosition(newnode,-1)

# print('Before:')

# print(ll)

# print('After adding:')

newnode=Node(3)
ll.addNodeAtPosition(newnode,2)

newnode=Node(3)
ll.addNodeAtPosition(newnode,-1)

# print(ll)

# ll.removeNodeAtPosition(2)

# print('After removing:')

# print(ll)


# ll.deleteNode(2)

print(ll)
ll.removeDuplicates()
print(ll)

