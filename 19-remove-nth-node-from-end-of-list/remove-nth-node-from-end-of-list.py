# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        curr=head
        while curr:
            l+=1
            curr=curr.next
        if l==n:
            nxt=head.next
            head=head.next
        index = l-n-1
        i=0
        cur=head
        while cur and cur.next:
            if i==index:
                temp = cur.next.next
                cur.next=temp
                cur=cur.next
                i+=1
            else:
                cur=cur.next
                i+=1
        return head