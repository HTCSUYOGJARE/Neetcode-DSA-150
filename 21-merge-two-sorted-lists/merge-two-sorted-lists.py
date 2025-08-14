# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None and list2==None:
            return list1
        elif list1!= None and list2==None:
            return list1
        elif list2!=None and list1==None:
            return list2
        if list1.val<=list2.val:
            newhead=list1
            curr1=list1.next
            curr2 = list2
        else:
            newhead=list2
            curr2=list2.next
            curr1=list1
        curr=newhead
        while curr1 and curr2:
            if (curr1.val>=curr.val) and (curr1.val <= curr2.val):
                curr.next = curr1
                curr1 = curr1.next
                curr = curr.next
            elif (curr2.val>=curr.val) and (curr2.val<=curr1.val):
                curr.next=curr2
                curr2=curr2.next
                curr=curr.next
        while curr1:
            curr.next = curr1
            curr1= curr1.next
            curr=curr.next
        while curr2:
            curr.next = curr2
            curr2=curr2.next
            curr=curr.next
        return newhead