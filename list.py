
#definging node class 
class node: 
     def __init__(self, data,number):
        self.data = data  # holding the data 
        self.next = None  # next pointer 
        self.number = number # number to hold the order 

class linked_list: 
    def __init__(self): #constructor 
        self.head= None # head and tail to null 
        self.tail = None

    def append(self,data,number):
        new_node=node(data,number)
        #conditions 
        if not self.head: # if the list is empty 
            self.head= new_node
            self.tail=new_node
        else: # add to the back 
            self.tail.next= new_node
            self.tail= new_node
    
    def push_front(self,data,number):
        new_node = node(data,number)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head = new_node
    def print_list(self):
        current_node = self.head
        while current_node:  # Traverse through the list
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")    