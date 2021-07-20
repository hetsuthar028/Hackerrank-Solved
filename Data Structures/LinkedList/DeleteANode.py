

#
# Complete the 'deleteNode' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def deleteNode(llist, position):
    # Write your code here
    if position == 0:
        h = llist.next
        llist = h
        return llist
    else:
        temp = llist
        ct = 0
        while llist:
            ct +=1
            
            if ct == position:
                break
            temp = temp.next
        else:
            return None
        
        tempNext = temp.next.next
        temp.next = tempNext
        return llist
    