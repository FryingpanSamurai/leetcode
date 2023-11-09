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
        # init vars
        myOutput = ListNode()
        ptr = myOutput
        carry = 0

        while l1 or l2 or carry:
            # extract values from nodes or use 0 if hte node is None
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # calc sum and update carry
            my_sum = x + y + carry
            carry = my_sum // 10 #int div will yield carry
            ones = my_sum % 10   #mod will yield ones

            # create a new node and advance the output list
            ptr.next = ListNode(ones) # creates a dummy node, but prevents us from creating a leading zero
            ptr = ptr.next

            # adv list if exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return myOutput.next
    

    
if __name__ == '__main__':
    test = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    l3 = ListNode(9, ListNode(9, ListNode(9)))
    l4 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))
    l5 = ListNode(5)
    myln = test.addTwoNumbers(l1, l2)
    while myln:
        print(myln.val)
        myln = myln.next