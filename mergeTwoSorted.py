from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoSorted(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mylist = ListNode()
        h1 = list1
        h2 = list2

        ## comparison between list1 and list2
        while h1 and h2:
            # compare
            if h1.val <= h2.val:
                # advance each node
                mylist.next = h1
                h1 = h1.next
            else:
                mylist.next = h2
                h2 = h2.next
            mylist = mylist.next

        # if list1 is bigger than list2- we need to append those missing values
        while h1:
            mylist.next = h1
            mylist = mylist.next
            h1 = h1.next

        # same story for list2
        while h2:
            mylist.next = h2
            mylist = mylist.next
            h2 = h2.next

        return mylist




if __name__ == "__main__":
    list1 = ListNode(1, ListNode(3, ListNode(5)))
    list2 = ListNode(2, ListNode(4, ListNode(6)))
    list3 = ListNode(9, ListNode(11))
    t_ob = Solution()
    t_ob.mergeTwoSorted(list1, list3)
