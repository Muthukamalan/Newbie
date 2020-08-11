'''
                                    LINKEDLIST
                            
        +---------------------------+        +----------------------------------+ 
        |         Node              |        |           LinkedList             |
        |---------------------------|        |----------------------------------|
        | [+] data                  |        |  [+] head                        |
        | [+] next                  |        |__________________________________|
        |___________________________|        |                                  |
        |                           |        |  [-] init(self)                  |
        | [-] init(self,data)       |        |  [-] reverse(self,preNode,cNode) |
        +---------------------------+        |                                  |
                                             |  [+] length(self)                |
                                             |  [+] addBegin(self,data)         |
                                             |  [+] add(self,data)              |
                                             |  [+] insert(self,data,pos)       |
                                             |  [+] delete(self)                |
                                             |  [+] delete_at_pos(self,pos)     |
                                             |  [+] find_node(self,data)        |
                                             |  [+] printf(self)                |
                                             |  [+] reverse_recur(self)         |
                                             |  [+] reverse_iter(self)          |
                                             |  [+] delete_LinkedList(self)     |
                                             +----------------------------------+            

'''

class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None


    def length(self): 
        current_node=self.head
        current_pos=0
        while True:
            if(current_node is not None):
                current_pos+=1
                current_node=current_node.next
            else:
                break
        return current_pos
        

    def addBegin(self,data):
        new_node=Node(data=data)               # data NODE created
        temp_node=self.head
        self.head=new_node
        self.head.next=temp_node
        del temp_node
        return


    def add(self,data):
        new_node=Node(data=data)               # data NODE created
        if(self.head is None):
            self.head=new_node
        else:
            last_node=self.head
            while True:
                if(last_node.next is None):
                    break
                last_node=last_node.next
            last_node.next=new_node
            return


    def insert(self,data,pos):
        new_node=Node(data=data)               # data Node created
        if(pos<0 or pos>self.length()):        # if N elements in array then (n+1) is invalid bcz array starts with 0
            print("Invalid Position")
            return
        elif(pos == 0):                        # POSITION is 0 goto addBegin
            self.addBegin(new_node)
            return
        else:
            current_node=self.head
            current_pos=0                       # index starts with Zero
            while True:
                if(current_pos==pos):
                    prev_node.next=new_node
                    new_node.next=current_node
                    break
                prev_node=current_node
                current_node=current_node.next
                current_pos+=1
            return
       

    def delete(self):                           # delete func normally delete at END
        last_node=self.head
        while last_node.next is not None:
            pre_node=last_node
            last_node=last_node.next
        pre_node.next=None


    def delete_at_pos(self,pos):
        if(pos<0 or pos>=self.length()):    #N elements there will be (n-1) index available
            print("Invalid Position")
            return
        if(pos == 0):
            self.head=self.head.next
            return
        if(self.length() !=0 ):
            current_node=self.head
            current_pos=0
            while True:
                if(current_pos==pos):
                    prev_node.next=current_node.next
                    current_node=None
                    break
                prev_node=current_node
                current_node=current_node.next
                current_pos+=1
            return


    def find_node(self,data):
        currentNode=self.head
        while (currentNode.data != data):
            currentNode=currentNode.next
            if(currentNode.next is None):
                print("Not found")
                return
        print("Found")
        return


    def printf(self):
        if(self.head is None):
            print('Your list is EMPTY')
            return
        else:
            current_node=self.head
            while True:
                if(current_node is None):
                    break
                print(current_node.data)
                current_node=current_node.next


    def __reverse(self,prev,cur):     # double underscore represent private func
        if cur is None:
            self.head=prev
        else:
            self.__reverse(cur,cur.next)
            cur.next=prev


    def reverse_recur(self):
        self.__reverse(None,self.head)       #Calling recursion func
        print('LinkedList is reversed by RECURSION!!!')
        return


    def reverse_iter(self):
        pre=None
        cNode=self.head
        while cNode:
            fNode=cNode.next
            cNode.next=pre
            pre=cNode
            cNode=fNode
        self.head=pre
        print("LinkedList is reversed by ITERATION!!!")
        return
    
    
    def delete_LinkedList(self):    #SoftDelete
        cNode= self.head
        while cNode:
            prev = cNode
            prev.next=None
            del prev
            cNode=cNode.next
        self.head=None
        return

    
if __name__=='__main__':
    #Linkedlist create
    L1=LinkedList()
    
    #Add NODE to LinkedList
    L1.add('value 1')
    L1.add('value 2')
    L1.add('value 3')

    #Add Beginning of LinkeList
    L1.addBegin('value 0')
    
    #PRINT LinkedList
    L1.printf()

    #LENGTH of LinkedList
    print("Length of LinkedList: ",L1.length())

    #Insert NODE to LinkedList
    L1.insert('value exceed',90);L1.insert('insuf value',-5)
    L1.insert('value 4',4)
    L1.insert('value inserted',2)

    #Delete NODE 
    L1.delete()
    L1.delete_at_pos(0)

    #Find NODE
    L1.find_node('value 1')
    L1.find_node('value 5')
    
    #Reverse LinkedList
    L1.reverse_recur()
    L1.printf()

    #RVERSER LinkedList
    L1.reverse_iter()
    L1.printf()

    #DELETE LinkedList
    L1.delete_LinkedList()   #Soft DELETE
    L1.printf()

    del(L1)         #Hard DELETE 
    try:
        print(L1)
    except NameError:
        print("Linked List is deleted!!")