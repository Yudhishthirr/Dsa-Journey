class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start==None

    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    
    def insert_at_last(self,data):
        n=Node(data)
        if(not self.is_empty()):
            temp = self.start
            while(temp.next!=None):
                temp=temp.next
            temp.next=n
        else:
            temp.next=n
    
    def search(self,data):
        temp = self.start
        while(temp!=None):
            if(temp.item==data):
                return temp
            temp=temp.next
        return None
    
    def insert_after(self,temp,data):
        if(temp!=None):
            n=Node(data,temp.next)
            temp.next =n
    
    def print_list(self):
        if(not self.is_empty()):
            temp = self.start
            while(temp!=None):
                print(temp.item,end=" ")
                temp = temp.next
        else:
            print("List is empty")
    
    def delete_frist(self):
        if(self.start!=None):
            self.start=self.start.next

    def delete_last(self):
        if(self.start is None):
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp = self.start
            while(temp.next.next!=None):
                temp=temp.next
            temp.next=None
    
    def delete_item(self,data):
        if(self.start is None):
            pass
        elif self.start.next is None:
            if(data==self.start.item):
                self.start=None
        else:
            temp = self.start
            if(temp.item==data):
                self.start=temp.next.next
            else:
                while(temp.next is None):
                    if(temp.next.item==data):
                        temp.next=temp.next.next
                        break
                    temp=temp.next

mylist = SLL()
mylist.insert_at_start(30)
mylist.insert_at_start(20)
mylist.insert_at_last(80)
mylist.insert_at_start(10)
mylist.insert_after(mylist.search(30),90)
print(mylist.search(30))
mylist.print_list()