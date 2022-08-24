class Node:

    def __init__(self,data,next=None) -> None:
        self.data=data
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
            return '->'
        op=''
        while temp.next:
            op=op+str(temp.data)+'->'
            temp=temp.next
        op=op+str(temp.data)
        return op

    def __iter__(self) -> None: 
        node=self.head
        while node:
            yield node.data
            node=node.next

    def append(self,node) ->None:
        if self.head is None:
            self.head=node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=node

    def remove(self):
        if self.head is None:
            return
        temp=self.head
        if temp.next is None:
            self.head=None
            return
        prev=None
        while temp.next:
            prev=temp
            temp=temp.next
        prev.next=None
            
    def addNodeAtPosition(self,node,pos) -> None: 
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

    def removeNodeAtPosition(self,pos) -> None:
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

    def deleteNode(self,node) ->None: # Delete node without refrence to head pointer of linked list
        temp=node.next
        if temp is None and self.head.next is not None: # Remove if its the last node of linked list
            self.removeNodeAtPosition(-1)
            return
        if temp is None and self.head.next is None: # Remove if there is only one node linked list
            self.removeNodeAtPosition(0)
            return
        node.data=temp.data # Copying the data of next node in the current node
        node.next=temp.next # Bypassing the current node
        temp.next=None # Removing link for the node
    
    def removeDuplicates(self,head) ->Node:
        map={}
        temp=head
        map[temp.data]=None                        # Adding head first in map
        while temp and temp.next:                  # Checking till 2nd last and last element
            if temp.next.data not in map.keys():   # Starting from head if next value is not in map
                map[temp.next.data]=None           # Add the next data value in map (for ex: head and next node is diff)
                temp=temp.next                     # Move temp to next node
            else:                                  # Next element data is in map (for ex: node and next node is same)
               temp.next=temp.next.next            # Skipping the node which is repeted (for ex: in 1,2,2,3 jumping from 1st 2 to 3)
        return head                                # Keep repeating logic i.e, keep jumping to next node untill new node is found

    @staticmethod
    def printUsingHead(head):
        while head:
            print(head.data,end=' ')
            head=head.next
        print(' ')


    @classmethod
    def convertListToLinkedList(cls,inputs):
        sll=SingleLinkedList()
        for val in inputs:
            sll.append(Node(val))
        return sll

if __name__=='main':

    ll=SingleLinkedList.convertListToLinkedList([2,2,2,2,2])
    print(ll)
    op=ll.removeDuplicates(ll.head)

    while op:
        print(op.data,end='-')
        op=op.next









                
                






    



