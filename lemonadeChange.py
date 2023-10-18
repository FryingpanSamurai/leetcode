class Solution:
  def lemonadeChange(self, bills: list[int]) -> bool: 
    """
      Instructions:
        Given array of bills: combo of 5, 10, 20
        Each customer only pays 5
        No change on hand at first
        Customers line up in a queue and order one at a time
        Determine if you can provide every customer with the correct change.
    """
    the_till = []
    lemonade_cost = 5

    for customer_bill in bills:
      change = customer_bill - lemonade_cost

      if customer_bill == lemonade_cost:
        the_till.append(customer_bill) # add the fiver to the till bud
      else:
        if not self.checkTill(change, the_till):
          return False
        the_till.append(customer_bill)
    return True

        

  def checkTill(self, change, till) -> bool:
    # check to see if the till contains bills for the change
    while change > 0:
      if change >= 10 and 10 in till:
        till.remove(10)
        change -= 10
      elif change >= 5 and 5 in till:
        till.remove(5)
        change -= 5
      else:
        return False
    return True


      

if __name__ == '__main__':
  test = Solution()
  bills = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,10,5,20,20,5,5,5,5,5,10,5,5,5,20,5,5,5,10,5,5,10,5,20,5,5,20,5,10,5,5,20,5,5,5,5,5,5,10,20,5,20,20,10,5,20,20,5,10,5,5,5,5,5,5,20,20,20,20,5,5,10,5,20,5,5,5,5,10,10,5,5,5,20,5,5,5,5,5,5,20,5,20,10,10,20,5,5,5,5,20,20,5,5,5,5,20,5,20,20,5,5,10,5,5,5,20,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,10,20,20,5,5,10,20,5,5,5,5,10,20,5,5,10,20,5,10,10,5,5,5,5,5,5,10,10,10,5,10,5,10,5,5,10,10,5,5,5,20,5,20,10,20,5,5,5,20,10,5,5,20,5,5,5,10,5,5,10,5,5,20,5,10,10,5,5,10,5,5,10,5,10,5,20,10,5,10,10,5,5,5,5,10,5,5,5,20,5,5,5,5,10,5,10,10,5,20,20,5,10,10,10,5,10,5,10,5,10,5,5,10,5,5,5,20,5,5,20,5,5,5,5,5,5,10,5,5,20,20,5,5,5,5,10,5,5,5,20,5,5,5,5,10,20,5,5,5,20,20,5,10,5,5,5,10,5,10,20,20,5,5,5,5,5,5,20,10,5,10,5,5,20,10,5,5,5,20,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5,5,5,10,10,5,10,5,10,20,10,10,5,5,20,10,20,5,5,5,10,5,5,5,10,5,20,20,20,10,20,5,5,5,5,20,5,20,5,10,5,5,5,5,5,5,20,5,10,5,5,5,20,5,5,5,10,10,5,5,5,5,5,20,20,20,5,5,5,5,20,5,20,5,20,20,10,10,5,5,5,20,10,20,10,20,5,20,5,5,5,10,10,5,5,5,5,10,10,5,5,5,5,20,5,5,5,5,5,20,10,20,20,5,20,10,5,5,20,5,5,10,5,5,5,5,10,5,5,5,20,5,10,5,10,10,20,5,20,5,20,10,5,5,5,20,5,10,10,5,5,10,5,10,5,5,20,20,5,5,5,5,5,5,5,5,20,5,10,5,10,20,20,5,5,20,5,10,5,20,5,20,20,5,5,5,20,20,20,5,5,5,5,20,10,5,5,10,10,10,5,10,5,10,5,20,5,5,5,5,10,20,5,5,5,5,5,5,20,20,10,10,5,5,20,5,5,5,5,20,20,20,20,5,5,20,20,5,20,5,5,5,10,20,10,5,20,5,5,5,5,10,10,5,10,5,5,10,5,5,20,10,20,5,5,5,10,5,5,10,10,5,20,5,5,20,5,5,20,10,10,5,5,10,5,5,20,5,10,5,20,20,10,10,20,5,5,5,20,5,5,20,20,10,20,10,10,5,20,10,5,10,5,10,5,5,20,5,20,20,5,5,5,5,20,10,5,5,5,5,5,20,5,5,20,10,5,5,5,5,5,5,10,5,10,5,20,20,20,20,5,5,20,5,5,5,20,5,20,5,5,5,10,5,20,5,5,5,5,20,5,20,20,5,5,5,5,10,5,20,20,5,20,5,10,5,5,5,5,20,5,5,5,20,20,5,5,5,20,10,20,5,5,10,5,5,10,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,20,5,20,10,20,20,5,5,10,10,5,10,10,5,5,10,10,5,5,5,5,5,10,5,20,5,10,5,20,10,5,10,5,10,20,10,5,5,5,20,5,5,20,5,5,5,5,5,10,10,20,20,20,5,20,20,5,20,5,5,5,5,5,5,20,5,5,5,5,10,5,5,5,5,10,20,20,5,5,5,5,5,5,5,10,5,5,5,5,5,5,5,5,5,5,5,10,20,20,5,5,5,5,5,5,20,5,5,5,20,5,5,20,5,5,5,5,5,5,5,10,5,10,5,5,5,20,5,5,5,20,5,20,5,20,10,5,5,5,5,10,5,10,5,20,20,10,5,5,20,10,10,5,10,20,5,5,5,10,5,20,5,20,5,5,5,5,5,5,5,5,5,10,5,5,5,20,5,5,10,10,5,5,10,5,10,10,20,10,20,5,5,5,10,10,5,5,20,5,20,5,5,5,5,10,5,20,5,5,5,20,5,5,10,10,5,5,5,20,5,5,10,5,5,5,5,20,5,10,5,5,10,5,10,10,5,10,10,5,20,20,5,5,20,5,5,5,5,5,20,10,10,5,10,5,20,20,5,5,5,5,5,10,5,20,10,20,5,20,5,20,20,5,5,5,5,5,5,5,5,5,20,5,10,5,5,20,20,5,20,20,5,5,5,10,20,5,5,10,10,5,5,20,10,20,5,10,5,5,5,5,20,5,5,5,5,20,20,5,20,5,10,10,5,10,20,20,20,5,5,5,20,5,5,5,5,5,5,5,20,20,5,5,5,5,5,5,5,5,5,20,5,5,5,5,20,10,5,5,5,5,20,5,5,5,5,5,5,5,5,20,10,5,5,5,5,5,10,5,20,5,5,5,5,10,5,10,20,10,20,5,5,5,5,10,5,20,5,20,5,20,5,10,5,10,10,10,5,5,5,20,20,5,5,10,10,10,5,5,20,5,5,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,10,5,5,5,5,5,5,5,20,10,10,20,10,5,5,5,5,5,5,20,5,5,20,5,10,5,20,5,10,5,5,20,5,5,5,10,5,5,5,10,5,5,20,20,5,5,10,20,10,20,5,10,20,5,5,10,5,20,20,5,5,5,5,5,5,5,10,10,10,5,20,20,5,5,20,20,10,20,5,5,5,5,5,5,10,5,5,20,5,20,20,10,5,5,5,5,10,5,10,5,5,5,5,10,20,20,5,5,5,5,20,5,5,5,5,10,20,5,5,10,5,5,10,5,10,20,20,5,10,5,10,5,5,10,10,5,5,5,5,5,5,20,5,20,20,5,5,5,5,5,10,5,5,5,5,5,5,5,20,10,10,5,5,10,5,20,5,5,10,10,20,5,5,5,20,10,5,5,5,10,5,5,5,5,5,20,5,10,5,5,10,20,5,5,20,10,5,5,20,5,5,5,5,10,5,5,5,5,5,5,10,10,5,5,5,5,10,5,20,5,10,10,5,10,5,5,5,5,5,5,10,20,5,5,20,20,5,20,10,5,5,5,10,5,20,5,5,10,20,5,5,20,10,20,10,5,5,5,10,5,5,5,5,5,10,20,10,5,5,5,5,5,5,5,5,20,10,5,20,10,5,20,10,20,10,5,20,5,5,5,5,5,20,20,10,10,10,10,5,5,20,5,10,5,5,10,20,5,5,5,5,20,5,5,5,10,5,5,10,5,20,20,10,10,5,5,10,5,5,10,5,5,20,5,5,5,5,5,5,5,5,5,20,5,10,5,5,5,5,10,5,5,20,10,10,5,20,20,20,5,5,5,5,20,5,10,5,5,5,5,5,10,20,5,20,5,20,5,10,20,5,5,5,5,5,5,5,10,5,20,5,5,20,5,5,5,5,5,20,10,5,10,10,5,20,10,5,20,20,5,5,20,5,5,10,5,5,10,5,5,10,10,5,5,20,10,5,20,5,10,5,5,5,5,5,5,20,5,5,5,20,5,10,5,10,20,10,10,5,5,10,5,20,10,5,5,5,5,5,10,5,5,5,5,5,10,20,20,5,5,5,20,5,5,5,5,10,5,20,5,5,5,20,10,5,5,5,5,10,5,5,5,10,5,5,5,5,20,5,5,5,10,20,20,20,5,20,5,10,5,10,20,5,5,20,5,5,5,5,5,5,5,5,5,20,20,10,5,20,5,5,5,5,5,5,10,5,5,10,5,5,5,5,20,5,5,5,20,5,5,10,5,10,5,10,20,5,5,5,5,20,10,5,5,5,20,5,10,10,5,5,10,20,5,10,5,5,5,20,10,5,20,5,5,5,20,20,10,20,10,5,20,5,10,10,20,10,5,5,10,5,20,20,5,5,5,5,10,5,10,20,20,20,10,20,5,10,5,5,5,10,5,5,5,5,10,5,5,5,20,10,20,5,20,5,5,5,20,10,5,5,20,5,10,5,5,5,10,5,5,10,10,5,20,20,20,5,5,5,5,20,5,20,20,5,10,5,20,5,10,20,5,5,10,5,5,5,5,5,10,10,5,5,5,20,5,10,5,5,5,5,5,20,5,10,10,5,5,10,20,10,5,5,5,5,10,5,5,10,5,10,5,10,5,20,5,5,10,5,20,5,5,10,5,20,5,20,20,10,5,20,10,20,20,5,20,5,20,5,5,20,5,5,5,5,10,5,5,5,5,5,5,5,5,20,20,10,5,5,20,20,20,10,20,20,20,10,10,20,5,10,5,5,10,5,5,5,20,10,20,20,20,5,5,5,10,5,5,5,20,10,5,10,5,5,10,5,5,5,20,5,20,5,5,5,5,5,10,20,10,5,5,5,5,5,10,5,5,5,5,5,10,20,5,10,20,10,10,5,5,20,5,20,5,5,20,5,20,20,5,5,5,10,20,5,5,10,5,5,5,5,5,10,5,5,5,20,5,5,5,5,5,10,5,5,5,5,10,5,20,10,5,5,10,5,5,10,10,10,5,5,10,5,10,5,20,10,20,10,20,20,10,5,10,10,10,5,20,5,5,5,5,10,5,5,20,20,10,10,10,5,10,5,5,20,5,5,5,5,5,5,20,5,5,10,20,5,5,5,20,10,10,10,20,20,10,5,5,10,20,20,10,5,5,5,10,10,5,20,5,10,20,20,5,5,20,10,5,20,5,5,10,5,5,5,10,5,5,10,5,5,10,5,20,5,5,20,5,5,5,20,20,5,20,20,5,5,10,5,5,5,10,5,5,5,5,5,5,10,5,5,10,5,5,5,5,5,5,5,20,5,5,5,5,5,5,20,20,5,10,5,5,5,5,5,10,5,20,10,5,5,20,5,5,5,5,5,5,5,5,20,5,5,5,20,5,10,5,5,20,5,5,20,20,20,20,5,10,5,20,5,5,20,5,5,5,10,5,10,5,20,5,5,5,5,20,5,5,20,20,5,5,20,5,5,5,20,10,5,5,5,5,5,20,20,5,5,5,5,5,10,10,5,10,10,10,5,5,5,20,5,20,10,20,20,5,5,10,5,5,5,10,5,5,5,5,5,5,5,5,10,20,5,5,5,5,5,5,10,10,5,10,10,5,10,5,20,10,10,5,5,20,5,5,10,10,10,5,10,10,10,5,10,5,5,10,5,10,20,20,5,20,5,5,5,10,10,20,5,5,5,10,5,5,5,5,5,20,5,5,10,20,5,20,5,5,10,20,10,20,5,10,5,5,5,10,20,10,5,10,5,5,5,20,5,5,10,5,5,5,5,5,20,10,10,5,20,5,20,5,5,10,5,5,20,5,20,20,10,20,10,5,20,5,20,20,20,5,5,5,10,5,20,20,10,5,20,5,5,5,20,10,5,5,20,20,5,20,20,5,5,5,5,5,5,5,5,10,10,5,5,5,20,5,5,10,20,5,5,5,5,5,5,5,5,20,5,20,5,5,5,5,5,20,5,5,10,10,20,5,20,5,5,5,20,10,5,5,5,5,10,5,20,5,5,5,5,20,20,10,5,5,5,10,5,20,5,10,5,20,5,10,5,5,5,5,5,20,20,5,5,5,5,5,20,10,20,5,5,5,10,5,5,5,20,5,5,5,20,5,5,5,5,5,5,5,10,5,5,20,5,20,5,5,20,10,5,5,5,5,5,5,5,5,5,10,10,5,10,5,10,5,5,10,5,5,10,10,20,5,20,5,5,10,20,5,5,5,5,5,5,20,5,5,5,5,5,20,5,10,5,5,10,5,5,5,5,5,5,20,5,5,5,20,5,5,5,20,10,5,5,10,5,10,5,20,5,10,5,5,20,5,10,5,5,5,10,5,5,5,5,5,20,5,5,5,20,5,10,5,20,5,5,5,10,5,10,5,5,5,5,5,5,5,5,5,5,5,5,10,10,5,20,20,5,5,10,5,5,5,5,10,10,10,5,5,20,5,10,20,5,5,5,5,5,10,10,5,20,5,10,5,5,5,5,20,5,20,10,20,10,10,20,5,5,5,5,5,10,5,5,20,5,5,10,5,5,5,20,20,20,5,10,20,20,10,20,20,20,5,10,20,5,10,5,10,5,20,20,5,5,5,5,5,5,20,5,5,5,5,5,5,5,20,10,5,5,20,5,5,5,20,5,10,20,10,20,5,20,5,5,5,5,20,5,5,5,5,20,5,5,5,5,20,5,5,20,5,20,10,5,5,5,20,10,5,5,5,20,5,10,5,5,5,5,10,5,20,5,5,5,5,5,5,5,5,10,5,10,5,5,5,10,10,5,5,10,20,20,20,20,5,10,5,5,5,5,5,5,5,5,10,10,5,5,20,5,20,5,10,20,5,10,20,5,20,5,10,20,5,20,5,20,20,5,10,5,20,5,5,5,20,10,5,5,5,5,5,5,5,5,10,10,20,5,5,5,5,5,5,5,10,20,10,10,10,20,5,5,10,20,5,20,20,10,5,5,20,5,20,5,20,10,5,10,5,5,5,5,5,10,5,5,10,5,5,20,5,20,5,5,5,5,20,5,5,5,5,5,5,5,10,5,10,20,5,20,5,10,10,5,5,10,5,20,20,5,5,5,10,20,5,5,5,5,10,5,5,5,5,20,5,10,10,5,5,20,5,10,5,20,10,10,5,10,20,5,5,10,5,5,10,5,5,5,5,10,5,5,5,10,5,10,20,20,5,10,5,20,5,10,5,5,20,5,5,20,5,5,20,5,5,10,20,5,5,5,20,20,20,5,20,10,5,5,5,5,5,5,10,5,20,5,10,5,20,5,20,5,20,5,10,5,20,20,10,5,5,10,20,5,5,20,10,5,5,5,5,5,5,5,5,20,10,10,10,10,5,5,5,5,5,10,5,5,5,5,5,5,5,5,5,5,20,5,5,20,20,5,5,5,5,5,5,10,5,20,20,10,20,5,5,5,5,10,20,5,20,5,5,20,5,5,5,5,5,20,20,5,5,5,10,5,5,10,10,10,20,10,5,20,5,5,10,20,5,5,10,5,5,20,5,20,5,5,5,5,5,5,20,5,20,5,5,20,5,5,5,5,20,5,5,5,5,5,20,5,5,5,10,20,10,5,20,20,5,20,5,5,5,5,5,5,5,10,5,5,20,5,10,10,20,10,5,5,10,5,5,10,10,5,5,5,5,5,20,10,5,5,20,5,5,20,5,10,10,20,20,20,10,20,5,20,20,5,5,20,5,20,5,5,20,5,20,5,5,10,5,20,10,5,5,5,5,10,5,20,5,20,20,20,5,10,5,5,5,5,10,20,10,10,20,5,10,5,5,10,5,20,5,20,10,20,5,5,5,5,20,20,5,5,5,10,10,5,5,5,5,5,5,5,5,5,10,5,20,5,5,5,20,5,10,20,5,20,5,5,5,10,5,5,5,5,5,5,5,10,5,10,20,5,5,5,5,5,5,10,5,10,5,10,5,5,5,10,10,20,5,5,10,20,5,20,5,20,10,5,5,5,20,5,10,5,5,5,5,5,20,20,10,5,5,10,5,5,5,10,5,10,10,5,5,5,10,5,10,5,5,5,5,5,10,5,10,10,10,10,5,5,5,5,5,20,10,5,5,5,10,5,5,20,5,5,10,5,5,10,10,10,5,10,20,5,5,20,5,20,5,5,20,5,5,20,20,5,5,20,10,5,5,5,5,5,5,5,10,5,20,5,10,5,5,5,5,5,5,5,10,5,20,10,5,20,5,5,5,5,5,5,20,5,10,5,5,10,20,20,5,5,20,5,5,20,5,10,20,20,5,5,5,5,5,5,20,20,5,10,5,5,5,5,5,5,5,5,20,10,5,5,5,5,5,5,5,5,5,5,20,5,20,20,20,5,5,5,10,10,5,5,10,5,5,5,10,10,5,5,10,10,10,20,5,20,5,5,5,5,5,5,5,10,10,20,5,5,5,5,5,5,5,5,10,5,10,10,5,10,5,5,5,5,10,10,20,10,20,5,10,20,20,20,5,5,10,5,20,20,5,20,20,5,10,5,5,10,20,5,5,5,5,5,10,5,10,5,10,20,5,5,5,5,5,20,10,20,10,20,20,5,5,20,20,5,5,10,5,5,5,20,10,10,5,5,20,5,5,5,20,10,10,5,5,5,10,5,10,10,20,5,10,5,20,5,5,5,20,10,20,5,10,5,20,10,5,5,5,5,5,5,5,20,5,5,20,5,20,5,5,20,5,10,5,5,5,5,5,5,10,5,10,5,5,20,5,10,5,5,5,10,10,5,5,5,20,5,5,20,20,5,5,10,20,5,5,5,5,5,10,20,5,5,10,20,10,20,5,10,5,5,20,20,5,5,5,10,5,5,10,5,5,5,20,20,10,5,5,20,20,5,20,5,10,20,5,5,5,10,5,5,5,10,5,5,20,10,5,20,20,20,5,5,10,5,20,20,20,20,10,5,10,10,10,5,5,5,20,5,10,10,20,5,5,5,5,5,20,5,5,20,10,5,5,20,10,5,10,10,20,10,20,5,5,5,10,10,5,5,10,20,20,5,5,5,10,5,5,20,5,5,5,5,5,10,20,10,5,10,5,5,5,5,5,5,10,5,5,10,10,5,20,5,10,5,5,5,10,5,5,10,20,10,10,20,10,10,20,5,5,5,5,10,5,5,20,20,5,10,20,10,5,5,20,5,20,20,5,5,5,10,5,5,5,5,20,5,5,5,5,5,5,5,5,5,10,10,5,5,5,20,5,5,5,10,20,5,5,5,5,10,5,10,20,5,10,5,5,5,20,5,20,10,5,5,5,5,20,5,5,5,10,5,5,5,5,10,20,5,5,5,10,20,10,10,5,5,20,20,20,10,20,20,10,10,5,5,5,10,5,20,20,5,5,20,20,5,5,20,5,20,5,5,5,5,10,5,10,5,5,10,5,20,5,5,10,10,5,10,5,5,5,5,5,10,5,5,10,10,5,5,5,5,5,20,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,20,10,20,10,5,5,10,5,5,5,5,5,10,20,20,5,5,5,5,5,5,5,5,5,5,5,5,5,10,10,5,5,10,5,10,20,20,10,5,5,20,5,10,5,5,5,5,20,5,10,20,5,5,10,20,5,5,10,10,20,5,5,5,5,5,20,5,5,5,10,5,5,5,5,5,5,5,20,20,5,5,5,5,5,5,10,10,20,5,5,20,10,5,5,20,20,20,20,20,5,20,10,5,20,5,5,5,5,10,5,20,5,5,10,5,5,10,10,20,5,5,20,5,20,20,5,5,5,5,5,5,5,10,20,10,20,10,5,5,5,10,5,20,20,10,10,20,20,5,5,20,5,10,10,5,5,20,5,20,5,5,5,10,5,5,20,5,10,5,10,5,10,5,10,10,5,20,5,20,5,10,5,5,5,5,20,5,20,5,5,20,10,5,10,10,5,5,5,5,10,5,10,5,10,5,10,20,5,5,10,5,10,5,10,10,20,20,20,20,10,5,5,5,20,5,5,10,10,20,10,5,5,5,5,5,5,5,5,5,10,5,5,5,5,5,20,10,10,10,10,20,10,5,5,5,5,10,20,5,5,5,5,20,5,5,5,10,5,5,10,5,10,10,5,5,5,5,20,20,20,5,20,5,5,10,10,20,5,5,5,5,20,5,20,20,5,5,5,5,5,5,5,5,5,5,10,5,20,20,10,20,5,5,5,20,10,5,10,10,20,20,5,20,10,5,5,5,20,5,5,10,5,5,5,20,10,5,5,5,10,20,5,20,20,5,20,5,5,10,10,10,5,5,20,20,5,5,20,5,5,10,20,10,20,5,5,20,5,10,5,5,5,5,5,20,5,5,5,5,5,20,20,5,20,5,5,5,5,5,5,20,5,5,5,5,5,20,5,20,5,5,20,5,10,5,20,20,5,10,5,5,5,5,10,5,5,5,5,10,5,5,5,10,10,5,20,20,5,5,5,20,10,5,5,5,5,5,10,20,20,20,10,10,5,5,20,10,5,10,5,5,5,5,5,20,5,20,20,5,5,5,10,5,10,10,10,5,5,10,5,5,5,5,5,5,20,5,5,10,5,5,5,5,5,5,10,5,20,20,5,5,5,20,5,5,5,5,10,5,5,10,5,20,5,5,5,20,5,5,5,5,5,5,5,5,10,10,5,10,5,5,5,20,5,10,5,5,10,5,5,5,5,5,20,5,5,5,5,5,20,5,20,20,5,5,5,5,5,10,10,20,5,5,10,5,10,20,10,5,5,5,5,5,20,5,5,5,5,20,20,5,5,5,5,5,20,5,5,20,5,10,20,5,5,5,10,5,10,5,20,10,5,10,5,5,20,20,5,10,5,5,5,10,5,5,20,10,10,20,5,20,5,5,20,5,5,10,20,5,10,20,5,5,5,5,5,5,20,5,10,5,5,20,5,5,20,5,10,5,10,10,5,5,20,5,5,10,5,5,5,10,5,5,5,5,20,5,20,10,5,5,20,5,20,5,5,5,5,5,5,20,5,20,20,5,10,10,20,20,5,5,5,5,5,20,20,20,5,10,5,5,10,5,20,10,10,20,5,5,10,5,5,10,5,5,5,20,5,5,20,5,5,5,5,20,10,5,10,10,10,10,10,5,10,5,5,5,20,10,20,10,5,5,10,5,5,5,5,5,5,5,5,5,20,10,5,5,5,5,5,20,5,20,5,5,20,5,5,20,5,5,5,20,10,20,5,5,10,5,5,5,20,20,5,10,5,5,20,20,5,5,5,10,5,10,5,5,5,20,10,10,5,5,5,5,5,5,5,20,20,5,20,5,10,5,20,10,5,5,10,5,5,5,5,5,5,5,20,20,10,10,5,5,20,5,10,5,5,5,10,5,20,5,5,5,5,5,5,5,10,5,10,5,5,5,5,20,20,5,20,5,20,5,20,5,5,20,5,5,10,20,5,20,5,20,5,5,5,10,10,5,5,20,5,5,10,5,5,10,5,5,5,10,5,5,5,5,5,5,5,10,5,5,10,10,5,5,5,5,10,5,10,10,5,5,5,5,5,5,5,10,5,5,5,5,10,5,5,5,10,5,5,5,10,5,20,5,20,10,5,20,5,5,5,5,5,5,5,5,10,20,5,10,5,5,20,10,5,5,5,10,10,10,5,5,5,5,5,5,20,10,20,20,5,5,20,5,5,5,5,20,5,10,5,10,5,5,20,5,20,5,5,5,5,5,5,5,5,5,10,5,20,10,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,10,5,20,5,5,5,5,5,5,5,5,10,5,10,10,5,10,5,5,20,5,5,10,5,5,10,20,10,5,20,5,5,5,20,20,5,10,5,5,5,5,10,10,10,20,5,10,5,5,5,5,5,5,5,5,10,5,5,5,5,20,5,10,5,5,5,5,10,5,5,5,20,5,5,20,5,5,5,5,5,10,20,5,20,5,10,10,5,5,20,5,5,5,5,5,20,5,5,5,20,20,5,20,5,5,5,5,20,5,5,5,5,5,20,5,5,10,5,5,5,10,20,20,5,5,5,5,5,10,5,20,20,5,5,5,20,10,5,5,5,10,5,5,5,5,20,20,5,20,10,10,20,5,5,20,5,10,20,20,10,5,5,20,5,5,5,5,5,5,5,5,20,5,5,20,5,5,5,20,5,20,5,5,5,10,10,20,5,5,5,5,10,10,5,20,5,20,5,5,5,5,20,5,20,10,5,20,5,10,10,5,20,5,5,5,10,20,5,5,5,5,5,10,5,5,5,5,20,20,5,20,5,5,10,20,5,10,5,5,5,5,5,5,5,20,5,5,5,10,5,5,5,5,5,5,10,5,20,5,5,5,10,10,20,5,5,5,5,5,5,20,5,5,10,20,20,5,10,20,5,5,20,10,20,5,10,5,5,20,10,5,5,20,10,5,10,10,5,5,20,20,5,20,10,5,5,5,5,5,20,5,5,10,10,10,10,5,5,5,5,5,5,5,20,20,5,20,5,10,20,5,10,5,5,5,10,5,20,5,5,5,5,5,5,10,5,5,5,10,20,5,5,10,5,20,20,10,10,5,5,5,5,10,20,5,10,5,20,10,5,5,20,5,20,10,5,5,5,5,5,10,5,5,5,20,5,20,5,20,5,5,20,10,20,5,20,5,20,5,10,20,20,5,5,5,5,5,10,5,5,5,5,5,5,10,5,5,5,20,5,10,5,5,20,5,5,10,5,5,5,5,20,5,10,5,5,5,5,5,5,5,10,10,5,20,20,5,5,5,5,20,5,20,5,5,5,5,5,10,10,20,20,5,5,5,20,5,5,5,5,5,10,5,5,5,5,5,10,20,5,5,5,20,5,10,5,5,5,5,5,20,5,5,5,10,20,20,5,10,10,5,5,10,5,5,20,10,10,5,5,10,5,5,20,5,5,5,5,20,5,10,10,5,5,10,20,5,5,10,5,5,5,5,5,5,5,10,5,10,10,10,5,20,10,5,5,5,5,5,20,5,5,5,10,20,5,5,5,5,5,10,5,5,5,10,5,20,20,5,20,20,20,5,10,5,5,5,5,20,20,5,5,5,10,5,5,5,10,10,5,5,5,5,5,5,5,10,5,10,5,5,5,5,20,5,20,5,20,5,5,20,5,5,5,20,10,5,5,5,5,5,5,5,10,5,20,5,5,5,5,20,20,5,20,5,10,5,20,5,5,5,5,5,5,5,5,5,5,5,20,20,5,20,10,10,5,5,5,10,5,20,5,20,5,5,5,10,5,5,5,5,5,5,20,10,5,10,5,10,10,10,5,5,5,5,5,10,20,5,5,5,5,5,20,10,10,10,5,10,20,20,20,5,5,10,10,10,20,5,20,5,20,5,5,5,5,20,5,20,5,5,20,5,10,5,20,5,5,5,5,5,5,10,5,5,10,5,20,5,5,5,20,20,10,5,5,20,5,10,5,10,5,5,5,5,20,5,20,5,10,20,10,10,5,5,5,20,5,5,5,5,5,10,5,10,5,5,5,20,20,5,5,10,10,10,5,5,5,5,10,5,5,5,5,20,20,10,5,5,5,5,5,5,20,20,5,10,5,10,10,10,10,5,10,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,10,5,10,5,5,5,5,5,20,20,10,20,10,5,5,5,20,5,5,5,20,10,5,10,5,20,5,10,5,5,5,5,5,5,20,5,5,10,5,5,5,5,5,5,5,10,20,10,5,5,5,5,5,10,5,5,5,5,5,5,5,5,5,20,10,10,5,20,5,5,5,10,5,5,10,20,10,5,20,5,20,5,5,20,10,5,20,10,5,5,5,5,10,20,5,20,20,5,5,20,10,5,5,5,10,5,10,20,5,5,5,5,5,10,10,10,10,5,10,20,5,5,20,10,10,10,20,20,20,5,20,10,5,5,10,5,5,10,5,5,5,10,5,10,5,20,20,20,5,10,10,5,5,10,5,5,5,10,20,5,10,10,10,10,20,20,5,5,20,5,5,5,5,10,5,10,5,10,5,10,10,20,5,10,5,10,20,5,5,5,10,5,10,5,5,10,5,5,5,5,10,5,20,5,5,5,5,10,10,5,20,5,5,5,10,5,10,20,5,5,20,10,5,5,5,5,5,20,5,5,5,5,5,5,5,5,10,5,5,10,20,5,20,5,10,5,5,10,5,10,5,5,5,20,10,5,5,5,5,20,10,5,5,5,5,20,5,5,5,10,5,10,5,5,5,5,10,5,5,5,5,5,5,10,5,5,5,5,10,5,20,10,20,5,5,20,10,5,5,10,10,10,5,10,20,5,5,5,5,10,5,20,5,5,5,5,5,10,5,5,5,5,20,5,20,20,5,5,10,5,5,20,10,10,5,10,20,5,10,5,5,5,10,5,5,20,5,20,20,5,5,5,20,5,5,20,5,5,5,20,5,5,5,10,5,10,10,20,20,5,5,20,5,10,20,10,5,5,5,5,10,5,5,20,5,5,5,5,5,5,10,20,20,5,5,10,20,5,5,5,10,5,5,5,20,5,5,20,5,5,5,5,5,5,5,5,20,20,5,5,5,5,5,5,20,5,5,20,10,5,10,5,5,20,10,10,5,20,20,5,5,5,5,5,5,5,20,10,5,5,5,20,10,10,5,5,5,10,10,5,10,5,5,5,20,10,5,10,20,5,5,5,5,5,5,5,5,5,5,5,5,5,5,10,5,5,5,5,20,10,5,5,20,20,5,20,5,10,5,10,20,10,5,10,5,5,20,5,5,5,5,20,5,10,5,5,5,20,20,5,10,10,5,10,10,20,10,5,5,10,20,5,5,10,5,5,5,20,5,5,5,5,5,20,5,20,10,10,5,5,5,20,5,5,20,10,5,5,5,10,5,10,5,5,5,10,5,5,20,5,10,5,10,10,5,5,10,20,20,5,5,10,10,10,5,5,5,10,5,5,5,10,5,10,5,10,20,5,20,10,20,10,5,5,5,20,5,5,20,5,5,5,5,5,10,10,5,5,5,5,10,5,5,20,20,5,10,5,5,5,5,20,5,5,20,5,10,20,20,20,5,5,20,5,10,5,5,5,5,20,10,20,10,5,5,5,10,20,5,20,5,20,10,20,20,5,10,10,5,20,5,20,5,20,5,20,5,20,20,5,5,5,5,20,20,5,5,10,5,5,20,5,5,5,10,10,5,5,5,5,5,20,20,5,10,10,10,20,5,20,20,5,5,20,20,5,5,5,10,5,20,20,10,5,5,10,5,10,10,5,5,10,5,5,5,20,5,10,5,20,5,20,5,5,20,20,10,20,5,5,5,5,5,5,20,10,5,5,5,5,5,10,20,5,5,20,5,5,5,5,5,5,20,5,5,10,10,5,5,20,20,5,5,5,20,5,5,5,5,5,5,5,20,5,5,5,10,10,5,10,10,5,5,10,10,10,20,10,10,5,5,5,10,5,5,10,10,5,10,5,5,5,10,20,5,20,20,10,5,10,5,10,5,5,5,5,5,5,5,5,5,5,5,10,10,20,5,5,20,5,5,10,20,20,20,5,5,5,5,10,10,5,5,5,5,5,20,20,5,20,5,5,20,5,5,5,5,5,5,5,20,5,10,20,5,5,10,5,5,5,20,20,5,10,5,10,10,5,5,10,5,5,20,20,20,20,5,5,5,10,20,10,10,10,5,10,5,5,20,5,10,5,10,5,5,20,5,5,20,5,20,5,20,20,5,20,5,5,20,5,5,5,20,5,10,5,5,20,5,20,5,20,20,20,5,5,20,5,5,10,10,5,5,5,5,10,10,5,20,10,20,5,5,5,5,5,5,5,5,5,5,5,5,10,5,5,10,5,20,5,5,20,5,10,20,5,5,10,5,5,5,5,10,5,20,5,20,5,5,5,10,10,5,5,10,5,20,20,10,5,10,5,5,5,10,5,10,5,5,10,10,5,5,20,10,5,5,5,20,5,5,20,5,5,5,20,10,10,20,10,5,10,5,5,10,5,10,10,5,5,20,10,5,10,5,5,20,20,5,20,5,5,5,5,5,20,10,5,5,5,10,10,10,5,5,20,5,5,10,5,5,5,20,5,5,5,10,5,20,10,5,5,10,5,5,10,5,5,10,5,20,5,5,5,5,20,5,20,20,5,5,5,5,5,10,10,5,5,5,20,5,20,10,5,20,5,5,5,5,5,5,10,10,5,10,10,5,5,20,5,5,20,20,10,20,5,10,5,20,10,10,10,5,5,10,5,10,5,20,5,10,5,5,10,5,5,5,10,5,5,10,10,20,5,5,5,5,5,5,5,5,5,5,5,20,5,10,5,5,5,5,5,5,5,20,10,5,5,10,5,5,10,10,20,20,5,10,10,5,5,5,5,20,5,5,5,5,5,5,10,5,5,5,10,20,20,5,5,20,20,5,10,20,10,5,5,10,20,10,5,20,10,10,5,5,5,5,10,5,5,5,5,20,5,5,10,10,5,20,20,5,20,10,5,20,5,5,5,20,5,5,20,20,20,5,20,20,5,10,5,10,5,5,5,10,5,20,10,5,5,5,5,20,10,5,10,10,5,5,5,5,5,5,20,20,10,10,5,10,20,20,5,20,5,20,10,5,5,5,5,10,5,5,5,5,20,5,5,5,5,5,20,5,5,5,20,10,10,20,5,5,20,10,10,5,10,5,10,5,5,20,5,5,5,5,5,10,5,10,5,5,5,5,5,20,5,10,10,10,5,5,5,10,5,20,5,5,5,10,5,5,5,5,10,5,10,5,5,10,20,5,5,10,10,20,20,20,20,10,20,5,5,5,5,5,5,5,20,5,10,5,10,20,5,20,5,5,5,5,5,20,5,5,5,20,5,20,20,20,5,5,10,5,5,5,5,5,5,5,5,10,5,20,10,5,10,10,5,5,20,20,10,5,10,10,20,10,5,5,10,10,5,10,5,5,5,10,5,5,10,10,10,5,20,5,20,5,5,5,5,5,5,5,5,5,5,5,5,5,10,5,5,5,5,10,5,10,10,5,5,5,20,10,5,5,10,20,20,20,5,10,10,20,20,5,20,5,5,20,5,10,5,20,20,10,5,5,10,5,5,5,10,5,5,10,10,5,20,5,10,10,5,5,10,10,5,5,5,5,10,5,10,20,5,5,10,5,20,5,20,5,5,10,5,5,5,5,5,5,5,20,20,20,5,20,5,20,10,5,5,5,5,5,5,20,5,20,5,5,5,5,10,5,5,5,5,20,5,5,5,10,5,5,10,20,5,20,5,10,5,20,20,10,20,5,10,5,5,10,10,20,5,20,5,20,5,20,20,20,5,20,5,20,5,5,10,20,5,10,5,5,10,5,5,20,10,10,10,5,5,5,5,5,10,5,10,10,20,5,5,5,5,5,10,10,10,5,10,20,20,5,5,20,20,5,20,5,5,5,10,10,5,5,5,10,20,5,10,5,5,10,5,10,5,10,10,5,20,5,5,10,5,5,10,10,20,5,20,20,20,5,5,10,20,5,20,5,20,5,5,10,5,20,10,20,5,10,5,10,10,5,20,5,20,5,5,5,10,5,5,20,5,5,5,5,5,10,10,20,5,20,20,5,5,10,5,5,20,5,5,10,5,5,5,5,5,5,5,5,5,10,5,5,5,5,5,5,5,5,20,10,20,5,5,5,10,5,20,5,10,5,5,10,5,5,5,10,10,5,5,10,5,5,20,20,20,5,5,20,20,10,5,5,10,5,5,5,20,5,5,20,5,20,5,20,5,5,5,10,5,20,20,5,10,10,5,5,5,5,5,5,10,20,5,5,5,20,5,5,5,20,5,5,5,5,10,20,10,5,5,5,10,5,20,20,10,10,5,10,5,20,20,5,5,5,10,5,20,5,5,20,5,5,10,20,5,20,20,5,5,20,20,20,20,5,5,10,5,20,5,5,5,5,10,5,5,5,5,10,5,5,5,10,5,5,5,5,5,5,5,10,20,20,20,5,5,10,5,5,10,5,5,20,5,10,5,10,10,5,5,20,5,10,20,5,5,10,20,5,5,5,5,5,5,5,10,5,5,10,5,5,10,10,5,5,20,5,10,5,20,5,20,20,5,20,5,5,5,5,5,20,5,5,5,5,5,20,10,20,10,5,20,20,10,5,20,5,5,5,5,5,5,5,5,10,20,5,10,5,5,5,5,5,5,5,5,10,5,5,20,10,5,5,10,10,5,5,5,5,5,5,5,5,5,20,20,20,5,5,20,20,10,5,10,5,10,5,5,5,10,5,5,20,5,20,5,10,10,5,5,5,10,5,5,5,5,5,5,5,20,5,20,5,5,5,20,5,20,5,5,5,5,5,20,5,5,20,5,10,5,5,20,5,5,5,5,5,10,10,10,5,5,5,10,10,5,20,5,10,5,5,5,5,20,20,20,5,5,5,20,20,10,5,5,5,10,5,5,5,5,5,20,5,5,20,5,10,20,5,10,5,10,10,10,10,5,10,5,5,5,5,5,5,20,5,5,5,20,5,5,20,5,5,5,20,5,5,5,5,5,10,10,5,5,5,5,5,20,10,10,5,10,10,20,10,5,20,10,10,5,5,20,5,5,5,5,20,5,5,5,5,10,20,5,20,20,5,20,5,10,10,5,5,10,20,5,5,5,5,20,20,5,5,5,5,10,5,5,10,5,5,5,5,5,10,5,5,10,5,10,10,10,10,5,20,5,5,5,10,5,5,5,5,5,5,5,10,5,5,5,5,20,10,10,5,5,5,5,5,20,5,5,5,20,5,10,10,5,5,5,5,5,20,5,20,5,5,5,5,5,10,5,10,5,5,5,5,5,10,5,5,10,5,5,5,5,5,5,10,5,5,5,5,5,5,20,5,5,5,10,20,20,5,20,20,10,10,5,5,5,5,10,10,5,10,5,10,10,5,20,5,5,20,5,5,10,5,20,5,5,5,5,20,5,5,20,5,10,5,5,20,10,10,20,10,20,20,10,20,5,10,5,20,10,5,10,5,5,10,5,5,20,5,5,10,10,10,5,5,20,5,5,5,20,5,10,10,5,5,10,5,5,5,5,5,5,5,5,20,5,5,5,10,5,5,5,20,5,20,10,10,20,20,5,20,20,10,20,5,5,5,20,5,5,5,5,20,5,10,5,10,5,5,5,20,20,5,5,10,20,10,5,5,5,10,10,5,10,20,10,10,5,5,5,20,5,5,5,5,5,5,20,5,20,20,5,5,5,20,20,5,5,20,5,10,20,20,5,20,10,10,5,5,5,10,5,10,5,5,5,20,5,20,10,5,5,5,5,5,5,5,10,10,10,5,10,5,5,5,20,20,20,5,5,5,5,5,20,5,20,5,5,5,5,5,20,5,5,5,5,10,10,5,10,20,5,10,20,10,5,5,5,5,20,5,10,5,20,5,5,5,20,5,5,10,5,5,10,5,10,10,5,5,5,5,20,5,20,20,10,5,5,5,5,5,5,5,10,5,5,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,20,5,10,10,5,5,5,20,5,5,5,20,10,20,5,5,20,10,5,5,5,20,10,5,20,5,5,5,20,5,5,5,20,5,20,5,10,5,5,10,10,10,10,5,5,5,20,20,5,5,5,5,5,5,5,20,5,5,5,5,5,10,5,5,5,5,5,5,5,5,20,20,5,5,20,5,5,5,5,20,5,5,10,10,5,5,5,5,10,5,5,20,5,5,5,20,5,5,5,5,20,10,5,5,5,5,10,5,5,10,20,5,5,20,5,10,5,5,20,10,5,5,20,10,20,20,5,5,20,10,10,20,5,20,5,10,10,10,5,10,5,10,5,5,5,10,5,5,10,5,5,20,20,10,10,5,5,10,20,5,5,5,10,5,10,5,5,5,5,5,5,20,5,5,10,5,5,5,5,20,5,5,5,20,5,20,5,5,5,10,5,10,20,5,20,5,10,20,10,5,5,20,10,5,10,5,10,20,20,5,20,5,5,10,5,10,20,10,20,10,5,5,5,20,5,5,5,5,5,20,5,10,10,5,20,5,5,5,20,10,5,10,5,5,5,5,5,10,10,5,5,10,20,20,20,5,10,5,5,5,20,5,5,5,20,5,5,5,5,10,5,5,5,5,10,20,5,20,5,5,5,5,20,20,20,5,5,10,20,5,5,5,5,5,5,5,10,20,5,5,5,20,5,5,10,20,20,10,5,5,5,5,20,5,5,20,20,5,5,10,20,5,5,20,5,5,10,5,10,5,10,20,10,5,5,10,5,5,5,5,5,5,20,20,20,5,5,5,5,10,20,5,10,20,5,5,5,10,20,5,10,5,5,5,5,5,10,5,5,5,20,5,5,20,5,20,5,20,10,10,5,5,20,5,5,5,5,20,20,5,5,20,20,5,5,5,10,20,5,5,5,5,5,5,10,5,5,5,10,5,5,5,5,10,5,5,5,20,5,5,10,5,5,5,5,20,10,10,5,10,10,5,20,5,5,5,5,10,5,20,20,5,5,10,10,20,20,5,5,5,5,5,5,5,5,20,5,5,20,5,5,10,10,20,5,20,5,20,10,5,20,10,5,10,5,5,5,5,5,10,5,5,20,5,20,5,5,20,10,10,5,10,10,5,10,5,5,5,10,10,5,5,20,10,10,10,5,5,20,5,5,20,5,5,5,20,5,5,5,10,10,5,5,5,20,20,20,5,20,5,20,5,10,5,5,5,20,5,20,10,20,5,10,5,5,20,5,5,20,10,5,5,5,5,10,10,5,5,20,20,5,10,20,5,10,5,20,5,5,10,10,5,5,5,20,5,5,5,5,10,20,5,10,5,20,5,5,5,10,5,5,5,5,20,20,5,5,10,20,5,5,5,20,5,5,10,5,10,20,10,20,10,20,5,5,20,5,5,5,5,20,10,5,5,5,5,5,5,5,5,20,5,20,5,20,10,5,10,10,20,10,20,5,10,10,20,5,5,5,5,5,5,5,20,20,5,20,20,20,5,5,5,5,10,5,5,5,5,20,5,5,20,10,5,5,5,5,5,5,20,5,5,5,10,10,5,20,10,20,10,20,5,5,5,20,5,5,5,20,10,20,5,5,5,20,5,5,5,5,5,20,5,5,10,5,5,5,5,5,20,20,5,5,5,5,5,5,5,5,20,10,5,5,20,5,5,20,20,20,5,10,10,5,5,5,5,10,20,10,10,5,5,5,5,5,20,10,5,20,10,5,10,5,5,20,5,5,5,10,5,5,5,20,5,20,5,5,5,5,5,5,5,5,10,10,5,10,10,5,5,5,20,5,5,10,5,5,5,20,20,20,20,5,5,5,5,10,5,20,5,5,20,20,5,5,20,10,10,5,5,5,20,5,5,5,5,5,10,5,20,20,5,5,5,10,20,5,20,5,20,5,5,5,5,5,5,5,20,20,20,5,5,20,20,10,5,5,5,5,5,5,5,5,20,5,20,10,20,5,5,5,5,5,5,10,5,5,10,5,5,5,5,5,20,5,5,5,5,5,10,5,5,10,10,5,10,10,5,5,20,20,5,5,5,5,5,10,5,20,10,5,5,5,5,5,5,5,5,5,10,20,20,5,20,5,20,20,20,10,20,10,5,5,10,10,20,5,5,5,5,5,10,5,10,5,5,5,5,5,5,20,5,5,5,20,20,20,10,5,5,10,5,5,10,5,5,20,10,20,5,5,20,20,10,20,20,5,5,5,5,5,5,5,10,5,10,10,5,10,5,20,20,10,10,5,5,20,10,5,10,10,5,5,5,5,10,5,5,20,5,5,5,5,10,5,10,5,10,5,5,5,5,10,5,5,20,5,5,5,5,5,10,20,5,10,5,10,20,10,20,20,5,5,5,5,5,20,5,10,10,5,20,5,20,10,20,10,5,10,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,20,5,5,5,10,5,5,5,5,5,5,5,10,5,10,10,20,5,20,5,5,20,5,20,5,5,5,20,10,10,5,5,5,5,5,20,10,10,5,5,5,20,10,5,10,5,5,20,10,5,5,5,5,5,5,20,5,20,5,10,10,5,5,5,5,10,5,5,5,5,10,5,10,5,10,5,10,5,5,5,5,20,5,5,20,5,5,10,5,5,5,5,10,5,5,10,5,20,5,5,5,10,10,5,20,5,5,10,5,5,10,20,5,5,5,5,10,20,20,20,5,5,10,20,5,5,5,10,5,20,5,5,5,20,5,5,5,5,5,5,20,5,20,5,10,5,20,20,10,10,5,5,10,5,5,5,5,5,5,10,20,10,10,5,5,5,5,5,20,5,5,5,5,5,5,5,5,10,5,20,10,20,20,5,5,5,5,5,5,10,5,5,5,10,20,10,20,5,10,5,5,5,5,5,5,10,10,5,5,10,20,10,5,5,5,5,20,5,5,20,5,5,10,5,5,5,5,5,5,10,20,5,20,20,10,10,10,20,10,20,5,5,10,10,5,20,5,5,10,5,5,5,5,5,5,5,10,20,10,10,5,10,20,5,5,20,5,10,5,5,10,5,20,10,10,10,5,5,5,5,5,5,5,20,5,5,20,10,5,5,20,5,5,5,5,20,20,5,10,5,20,5,5,5,5,5,5,20,10,20,20,10,5,5,5,5,5,5,20,5,10,5,5,5,5,5,10,5,5,5,20,20,5,10,20,20,20,10,20,5,5,5,5,20,5,5,5,5,20,5,5,5,5,20,5,20,5,5,5,5,5,5,10,5,5,5,5,5,10,5,10,5,10,5,5,20,10,20,10,20,5,5,5,5,5,10,20,10,20,20,10,5,5,10,5,5,10]
  print(test.lemonadeChange(bills))