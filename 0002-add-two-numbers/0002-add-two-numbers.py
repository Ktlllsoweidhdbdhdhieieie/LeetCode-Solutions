# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0) #chain ka shuruaavat l ahhok jo ek jagah fuixed hai
        current=dummy #ek worker jo lopp ke haar chakre pr naya node jodta hai aur khud aage badh jata hai
        carry =0 #starting me carry 0 hoga
        while l1 or l2 or carry: # jak tak saare digit ya carry khatam nhi hote ye chalta rahega
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
             #total sum
            total=val1+val2+carry
            carry=total//10 # agar sum10 ya greater than 10 hai to carry is 1
            new_digit=total%10 # niche likhne wala number jo node me jayega

            current.next=ListNode(new_digit)
            current=current.next
            if l1: l1=l1.next
            if l2: l2=l2.next
        return dummy.next #duumy ke aage se hamara original ans start hota hai
