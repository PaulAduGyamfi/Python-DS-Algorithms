'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


'''





# ---------- SOLUTION -------------- #
#                                    #
#                                    #
#                                    #
#                                    #
# ---------------------------------- #
def removeNthFromEnd(self, head, n: int):
        fast = head
        slow = head
        prev = None

        if head.next is None:
            return None
       
        for _ in range(n):
            if fast is None:
                return None
            fast = fast.next
        
        if fast is None:
            head = head.next
            return head
        
        while fast is not None:
            prev = slow
            slow = slow.next
            fast = fast.next
        prev.next = slow.next
        return head