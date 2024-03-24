#Peanut butter jelly time
#Peanut butter jelly time
#Peanut butter jelly time
#Where he at? Where he at?
#Where he at? Where he at?
#Now there he go
#There he go
#There he go
#There he go
#Peanut butter jelly
#Peanut butter jelly
#Peanut butter jelly with a baseball bat

# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head == ListNode():
            return ListNode(val='')
        values = []
        while head.next != None:
            values.append(head.val)
            head = head.next
        values.append(head.val)
        #print(values)
        node = ListNode(values[0])
        for i in range(len(values)-1):
            prev_node = node
            node = ListNode()
            node.next = prev_node
            node.val = values[i+1]

        return node