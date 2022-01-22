# # Creation


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# class Slinkedlist:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def printll(self):
#         node = self.head
#         while node:
#             print(f'-> {node.value}', end=" ")
#             node = node.next

#     # Insertion
#     def insertion(self, value, location):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             if(location == 0):
#                 new_node.next = self.head
#                 self.head = new_node
#             else:
#                 last_node = self.head
#                 while(last_node.next):
#                     last_node = last_node.next

#                 last_node.next = new_node
#                 new_node.next = None

#     def middle(self, value, location):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node

#         else:
#             curr_node = self.head
#             index = 0
#             while (index < location):
#                 curr_node = curr_node.next
#                 index += 1

#             next_node = curr_node.next
#             curr_node.next = new_node
#             new_node.next = next_node


# if __name__ == '__main__':

#     singlylinklist = Slinkedlist()
#     # singlylinklist.insertion(2, 0)
#     # singlylinklist.insertion(1, 0)
#     # singlylinklist.insertion(4, 1)
#     # singlylinklist.insertion(5, 1)
#     singlylinklist.middle(9, 0)
#     singlylinklist.middle(9, 0)
#     singlylinklist.middle(5, 1)

#     singlylinklist.printll()


#           Traversal


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def traverse(self):
        node = self.head
        if self.head is None:
            print('Null link list')
        else:
            while (node):
                print(f'-> {node.value}', end="")
                node = node.next


if __name__ == '__main__':

    vivek = SLinkList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    vivek.head = node1
    vivek.head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    vivek.traverse()
