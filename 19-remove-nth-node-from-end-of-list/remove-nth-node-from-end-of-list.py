# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # first lets get the length of the singly-linked list
        l=0
        curr=head
        while curr:
            l+=1
            curr=curr.next

        # get the index from start at which we need to skip the next node
        index = l-n-1
        i=0
        cur=head
        while cur:
            if i==index:
                temp = cur.next.next
                cur.next=temp
                cur=cur.next
                i+=1
            elif index==-1: # if n==l (index=n-l-1--> -1) means to remove first node of linked list then directly return head.next
                return head.next
            else:
                cur=cur.next
                i+=1
        return head