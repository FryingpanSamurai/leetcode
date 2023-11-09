from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    """
    FUNCTION: Given two linked lists, add the two numbers and output that into a separate linked list
    INPUT:    list1 as Linked List, list2 as Linked List
    OUTPUT:   Sum of two numbers as Linked List
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # what do we need to do first
        # init vars
        myOutput = ListNode()
        ptr = myOutput
        carry = 0

        # loop thru shortest list or where both lists exist
        while l1 and l2:
            # add the two values
            # don't forget about the carry value
            my_sum = l1.val + l2.val + carry

            # separate out the carry and the ones
            carry = int(str(my_sum)[0]) if len(str(my_sum)) > 1 else 0
            ones = my_sum if my_sum < 10 else int(str(my_sum)[1])

            # assign ones and adv output listnode and both lists
            ptr.val = ones

            # adv lists and append new Node
            # needs to be conditional so there are no leading zeroes
            if l1.next or l2.next:
                ptr.next = ListNode()
                ptr = ptr.next
            l1 = l1.next
            l2 = l2.next
        
        # append the rest of the longer list
        # remember you have to account for carry
        while l1 or l2:
            my_sum = l1.val + carry if l1 else l2.val + carry
            # separate out the carry and the ones
            carry = int(str(my_sum)[0]) if len(str(my_sum)) > 1 else 0
            ones = my_sum if my_sum < 10 else int(str(my_sum)[1])
            ptr.val = ones

            if (l1 and l1.next) or (l2 and l2.next):
                ptr.next = ListNode()
                ptr = ptr.next
            # conditional because l1.next could be None and so None.next will throw an exception
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # append dangling carry: append node, then assign value
        if carry > 0:
            ptr.next = ListNode()
            ptr = ptr.next
            ptr.val = carry

        return myOutput
    

    
if __name__ == '__main__':
    test = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    l3 = ListNode(9, ListNode(9, ListNode(9)))
    l4 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))
    l5 = ListNode(5)
    myln = test.addTwoNumbers(l5, l5)
    while myln:
        print(myln.val)
        myln = myln.next