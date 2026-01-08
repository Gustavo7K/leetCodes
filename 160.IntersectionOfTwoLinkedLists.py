class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        
        currentA = headA
        lenghtA = 0
        tailA = None

        while currentA:
            lenghtA += 1
            tailA = currentA
            currentA = currentA.next
        
        currentB = headB
        lenghtB = 0
        tailB = None

        while currentB:
            lenghtB += 1
            tailB = currentB
            currentB = currentB.next
        
        if tailA is not tailB:
            return None

        delta = abs(lenghtA - lenghtB)

        currentA = headA
        currentB = headB

        if lenghtA > lenghtB:
            for _ in range(delta):
                currentA = currentA.next
        else: 
            for _ in range(delta):
                currentB = currentB.next
        
        while currentA and currentB:
            if currentA is currentB:
                return currentA
            currentA = currentA.next
            currentB = currentB.next
        return None