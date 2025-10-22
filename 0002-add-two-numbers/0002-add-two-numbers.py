# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
      
        i=0
        j=0
        num1=0
        num2=0
        dummyHead = ListNode(0)
        curr = dummyHead
        while (l1 != None):
            num1=num1+l1.val*(10**i)
            i=i+1
            l1=l1.next
        while (l2 != None):
            num2=num2+l2.val*(10**j)
            j=j+1
            l2=l2.next
        tol=num1+num2
        cal=10
        leng=len(str(tol))
        for i in range(leng):
            j=tol%10
            tol=tol//10
            newNode= ListNode(j)
            curr.next=newNode
            curr=newNode
        return dummyHead.next


            


        