from single_linked_list import SingleLinkedList,Node

def mergeTwoSortedLinkedList():
    # Merge two sorted linked list without extra space

    head1=SingleLinkedList.convertListToLinkedList([1,4]).head
    head2=SingleLinkedList.convertListToLinkedList([2,3]).head

    temp=None
    prev=None
    listHead=None
    if head1.data<head2.data:
        temp=head1
        listHead=head2
    elif head2.data<head1.data:
        temp=head2
        listHead=head1

    start=temp
    prev=temp
    temp=temp.next

    while temp.next or listHead.next:
        # if temp.next.next is None:
        #     pass
            
        if prev.data<listHead.data<temp.data:
            node=listHead
            listHead=listHead.next
            prev.next=node
            node.next=temp
            prev=prev.next
            SingleLinkedList.printUsingHead(start)
            continue
        if listHead.data>temp.data and listHead.data>temp.next.data:
            prev=temp
            temp=temp.next
            SingleLinkedList.printUsingHead(start)
            continue
        if temp.data<listHead.data<temp.next.data:
            node=listHead
            listHead=listHead.next
            nextNode=temp.next
            temp.next=node
            node.next=nextNode
            prev=temp
            temp=temp.next
            SingleLinkedList.printUsingHead(start)
            continue


    if temp.next is None:
        temp.next=listHead

    SingleLinkedList.printUsingHead(start)

def reverseList():
    head=SingleLinkedList.convertListToLinkedList([1,1]).head

    tail=head
    temp=head
    start=head
    while tail.next:
        tail=tail.next
    temp=temp.next
    tail.next=start
    start.next=None
    while temp!=tail:
        node=temp
        temp=temp.next
        tail.next=node
        node.next=start
        start=node
        


    SingleLinkedList.printUsingHead(tail)


reverseList()

    

    
    



        



