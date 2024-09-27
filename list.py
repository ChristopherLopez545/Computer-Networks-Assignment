
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

    def inorder_Insert(self,num,data): # num here is the sequence number 
        #insert node into linked list 
        new_node = node(data,num)
        if self.head is None or self.head.number > num: # if head is null or is greater then the current 
                                                        # sequence number 
            new_node.next= self.head #this pushes at the front 
            self.head = new_node
            return

        current = self.head
        # this part finds where the current word should be inserted 
        while current.next is not None and current.next.number < num:
            current = current.next # traverse 
        
        new_node.next = current.next 
        current.next = new_node

        
    # this method is used to assemble the words in correct order 
    def put_together(self):
        #empty list 
        word_list = [] 
        curr = self.head
        while curr: 
           # print(curr.data)
            word_list.append(curr.data) # add the data at the head 
            curr= curr.next # point to the next object 
        
        #return the word list into a single string 
        return " ".join(word_list)
        

