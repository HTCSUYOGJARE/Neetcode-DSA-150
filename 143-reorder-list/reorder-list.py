# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        second = slow.next #taking the only second half of linkedlist
        slow.next = None  #cutting off the link between first and second half

        # firstly reversing the second half of linked list
        prev,curr=None,second
        while curr:
            temp =curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        #using the reversed second half and the normal first half, merging them alternately
        forward,reverse=head,prev
        while reverse:
            temp_for=forward.next
            temp_rev=reverse.next
            forward.next=reverse
            forward.next.next=temp_for
            forward=temp_for
            reverse=temp_rev
            
    