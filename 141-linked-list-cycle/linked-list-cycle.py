# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        S=set()
        while curr:
            if curr not in S:
                S.add(curr)
                curr=curr.next
            else:
                return True
        return False





        