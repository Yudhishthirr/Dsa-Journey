class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class DLL:
    def __init__(self,start=None):
        self.start=start
    
    def is_empty(self):
        return self.start==None
    
    def insert_at_start(self,data):
        n=Node(None,data,self.start)
        if(not self.is_empty()):
            self.start.prev=n
        else:
            self.start = n
    

    def insert_at_last(self,data):
        temp = self.start
        if(self.start!=None):
            while(temp.next!=None):
                temp=temp.next
        n=Node(temp,data,None)
        if(temp==None):
            self.start=n
        else:
            temp.next=n

    def search(self,data):
        if(not self.is_empty()):
            temp = self.start
            while(temp!=None):
                if(temp.item==data):
                    return temp
                temp=temp.next
            print("Data not found")
        else:
            print("List is empty")


    def insert_after(self,temp,data):
        if(temp!=None):
            n=Node(temp,data,temp.next)
            if(temp.next!=None):
                temp.next.prev=n
            temp.next=n

    def print_list(self):
        if(not self.is_empty()):
            temp = self.start
            while(temp!=None):
                print(temp.item,end=" ")
                temp = temp.next
        else:
            print("List is empty")

mylist = DLL()
mylist.insert_at_start(15)
mylist.insert_at_start(30)
# mylist.insert_at_last(mylist.search(50),90)
mylist.print_list()