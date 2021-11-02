# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1r = 0
        l2r = 0
        
        decimal = 1
        while l1:
            l1r += l1.val * decimal
            l1 = l1.next
            decimal *= 10
        
        decimal = 1
        while l2:
            l2r += l2.val * decimal
            l2 = l2.next
            decimal *= 10
            
        s = l1r + l2r
        l = [int(a) for a in str(s)]
        l.reverse()
        
        return listToNode(l)
        
        
def listToNode(l):
    head = None
    while l:
        head = ListNode(l.pop(), head)
    return head
