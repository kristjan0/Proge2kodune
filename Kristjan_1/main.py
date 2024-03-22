# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        values = []
        while head.next != None: #Loopdy loop until no more nodes
            values.append(head.val) #Write values into list
            head = head.next
        values.append(head.val) #Write last value into list as while quits on the last node
        #print(values)
        pikkus = len(values)-1 #Get the length of the list for index
        for i in range(len(values)):
            #print(values[i])
            #print(values[pikkus])
            if values[i] != values[pikkus]: #Return false if values on the opposite ends of the list are not equal
                return False 
            pikkus -= 1
        return True #Return true if we haven't returned false xD