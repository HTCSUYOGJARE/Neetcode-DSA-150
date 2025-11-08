# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2

        if not curr1:
            return curr2
        if not curr2:
            return curr1
        if curr1.val<=curr2.val:
            new_head=curr1
            curr1=curr1.next
        else:
            new_head=curr2
            curr2=curr2.next
        new_ll = new_head
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                    new_ll.next = curr1
                    new_ll = new_ll.next
                    curr1=curr1.next
                
            else:
                    new_ll.next = curr2
                    new_ll = new_ll.next
                    curr2=curr2.next    
        while curr1:
            new_ll.next=curr1
            curr1=curr1.next
            new_ll = new_ll.next
        while curr2:
            new_ll.next=curr2
            curr2=curr2.next
            new_ll = new_ll.next
        return new_head