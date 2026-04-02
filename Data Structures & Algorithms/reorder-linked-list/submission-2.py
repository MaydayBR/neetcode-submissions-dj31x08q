# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next  #second is the second part of the list 
        slow.next = None    #slow is first part of list

        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        #prev is the second part of the list reversely sorted 

        first,second = head,prev
        while second:
            temp1, temp2 = first.next , second.next

            first.next = second
            second.next = temp1

            first,second = temp1,temp2



