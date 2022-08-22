class Node:

    def __init__(self,value,next=None) -> None:
        self.value=value
        self.next=next

class SingleLinkedList:

    def __init__(self) -> None:
        self.head=None

    def __len__(self) -> int:
        temp=self.head
        if temp is None:
            return 0
        else:
            count=0
            while temp:
                temp=temp.next
                count=count+1
            return count

    def __repr__(self) -> str:
        temp=self.head
        if temp is None:
            return ''
        op=''
        while temp.next:
            op=op+str(temp.value)+'->'
            temp=temp.next
        op=op+str(temp.value)
        return op

    def __iter__(self) -> None: 
        node=self.head
        while node:
            yield node.value
            node=node.next

    def add_node(self,node,pos) -> None: 
        if self.head is None:
            self.head=node
        else:
            if pos==0:
                node.next=self.head
                self.head=node
            elif pos==-1:
                temp=self.head
                while temp.next:
                    temp=temp.next
                temp.next=node
            elif pos>0:
                count=0
                temp=self.head
                while count<pos:
                    temp=temp.next
                    count=count+1
                node.next=temp.next
                temp.next=node

    def remove_node(self,pos) -> None:
        if self.head is None:
            return
        else:
            if pos==0 and self.head.next is None:
                self.head=None
                return
            elif pos==0 and self.head.next is not None:
                temp=self.head
                self.head=temp.next
                temp.next=None
            elif pos==-1:
                temp=self.head
                prev=None
                while temp.next:
                    prev=temp
                    temp=temp.next
                prev.next=None
            elif pos>0:
                temp=self.head
                prev=None
                count=0
                while count<pos:
                    prev=temp
                    temp=temp.next
                    count=count+1
                prev.next=temp.next
                temp.next=None
                
                






    



