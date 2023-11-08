from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  """
  FUNCTION: given a singly linked list, reverse the order
  INPUT:    <linked list>
  OUTPUT:   reversed INPUT
  """
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
  myNode = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
  outNode = test.reverseList(myNode)
