'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 
Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

'''





# ---------- SOLUTION -------------- #
#                                    #
#                                    #
#                                    #
#                                    #
# ---------------------------------- #

def deleteDuplicates(self, head):

        if head is None:
            return None

        if head.next is None:
            return head

        pointerA = head
        pointerB = head.next
        
        while pointerB is not None:
            if pointerB.val == pointerA.val:
                next_node = pointerB.next
                pointerA.next = next_node
                pointerB = next_node
            else:
                pointerA = pointerA.next
                pointerB = pointerB.next
        
        return head