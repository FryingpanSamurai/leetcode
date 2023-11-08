from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  """
  FUNCTION: create an algorithm that takes two input ListNodes
            and merges them, sorted, asc.
  INPUT:    list1 as sorted ListNode, list2 as sorted ListNode
  OUTPUT:   a single sorted ListNode of merged list1 and list2
  """
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
    # two lists come in
    # the max we'll have to traverse is the shortest list
    # don't forget you have to append the remaining bits of the longest list
    # what do we do first
    # create variables
    sortedLN = ListNode()
    ptr = sortedLN #pointer
    
    # lets look at the val of the first node on each ListNode
    while list1 and list2:
      # sort
      if list1.val < list2.val:
        # connect current node to list1
        ptr.next = list1
        # 'advance' the list
        list1 = list1.next
      else:
        ptr.next = list2
        list2 = list2.next
      ptr = ptr.next # adv ptr

    ptr.next = list1 if list1 else list2

    # sorted list started at pos2
    return sortedLN.next 



if __name__ == '__main__':
  test = Solution()
  myl1 = ListNode(1,ListNode(3,ListNode(5)))
  myl2 = ListNode(2,ListNode(4,ListNode(6)))
  out = test.mergeTwoLists(myl1, myl2)
  while out.next:
    print(out.val)
    out = out.next