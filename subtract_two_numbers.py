"""
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
"""
class solution:
    def reverseLL(self, head):
        cur = head
        prev = None
        while cur:
            front = cur.next
            cur.next = prev
            prev = cur 
            cur = front
        return prev
        
    def subtractTwoNumbers(self, Node, a, b):
        temp1 = self.reverseLL(a)
        temp2 = self.reverseLL(b)
        ans = Node(-1)
        cur = ans 
        borrow = 0 
        
        while temp1 or temp2:
            diff = borrow
            
            if temp1:
                diff += temp1.data
            if temp2:
                diff -= temp2.data
            if diff < 0:
                diff += 10 
                borrow = -1
            else:
                borrow = 0 
                
            cur.next = Node(diff)
            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next
            cur = cur.next
            
        result = self.reverseLL(ans.next)
        
        while result.next and result.data == 0:
            result = result.next
        return result