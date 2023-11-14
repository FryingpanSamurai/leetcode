from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    FUNCTION:   Given two non-empty linked lists, with the most significant digit first, add the two lists 
                as if the linked list and their nodes were deconstructed numbers 7243 as (7)->(2)->(4)->(3)
    OUTPUT:     Output sum of the two lists as ListNode
    INPUT:      L1 as ListNode, L2 as ListNode
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # STEPS
        # 1 init vars
        outputLN = ListNode()
        ptr = outputLN
        carry = 0

        # 2 Determine Logic and algo
        # Goal: add two numbers in reverse order (reverse logic)
        # epistemology: get a pointer that navigates to end then add
        # we would have to renavigate through the singly linked list back to last pos - 1
        # this would result in n! looping INEFFICIENT...

        # hmmm the only other way, would be to get the linked list and throw it into a reverse order
        # then do the calculation
        # i don't know how else to do that....
        # FL: think stacks...
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

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
            
        return self.reverse(outputLN.next)
    
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ### What is the first thing we need to do
        # instantiate variables
        reversedList = ListNode()

        # the end becomes the start or vice versa
        # start at the end and start to connect the nodes backward
        # ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
        while head:
            # new list will be current head val and then the rest of the linked list we already have
            reversedList = ListNode(head.val, reversedList.next)
            head = head.next #adv the head
            reversedList = ListNode(0,reversedList) # attach a new placeholder Node to the head of the new list


        return reversedList.next # Linked list starts at Node 2
if __name__ == '__main__':
    test = Solution()
    l1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    myln = test.addTwoNumbers(l1, l2)
    while myln:
        print(myln.val)
        myln = myln.next