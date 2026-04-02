# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #solve using an array 
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
        
        l,r = 1,len(arr)-1
        prev_left = True
        curr = head
        while l <= r:
            if prev_left:
                curr.next = arr[r]
                r-=1
                prev_left = False
            else:
                curr.next = arr[l]
                l+=1
                prev_left = True
            curr = curr.next

        curr.next = None
