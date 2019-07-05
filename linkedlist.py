class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printElement(self):
        cur_node=self.head
        while(cur_node):
            print(cur_node.data)
            cur_node=cur_node.next 
    def append(self,data):
        newNode=Node(data)
        if(self.head is None):
            self.head=newNode
            return
        lastnode=self.head
        while(lastnode.next):
            lastnode=lastnode.next
        lastnode.next=newNode
    def prepend(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
    def inbwt(sefl,prev,data):
        if not prev:
            return
        newNode=Node(data)
        newNode.next=prev.next
        prev.next=newNode 

llist=LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepend("E")
llist.inbwt(llist.head.next,"Z")
llist.printElement()
