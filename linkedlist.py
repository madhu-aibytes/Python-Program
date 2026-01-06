class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
n1 = Node(10)   # creating of the nodes
n2 = Node(20)
n3 = Node(30)

n1.next = n2    #connecting the nodes to thenext node
n2.next = n3

temp = n1       # traversing,printing the linked list
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
