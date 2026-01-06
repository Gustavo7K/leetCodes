#Design a HashMap without using any built-in hash table libraries. Implement the MyHashMap class.
'''
- key: This is the input data (or, more commonly, the integer hash value derived from the original key using a hash function) 
that you want to store or retrieve in the hash table.
- % (Modulo Operator): This operator returns the remainder of the division of the key by self.capacity.
- self.capacity: This refers to the current size (number of available slots or "buckets") of the hash table's internal array.
- index: The result of the operation is an integer that falls within the range [0, self.capacity - 1], which corresponds directly 
to a valid index in the array.
- And i used linked lists along with all of that to solve this problem. 
'''

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap(object):
    def __init__(self):
        self.capacity = 1000
        self.buckets = [None] * self.capacity


    def put(self, key, value):
        index = key % self.capacity

        if self.buckets[index] is None:
            self.buckets[index] = ListNode(key, value)
            return

        current = self.buckets[index]

        while current:
            if current.key == key:
                current.value = value
                return
            if current.next is None:
                break
            current = current.next

        current.next = ListNode(key, value)

    def get(self, key):
        index = key % self.capacity

        current = self.buckets[index]

        while current:
            if current.key == key:
                break
            current = current.next
        
        for i in range (self.capacity):
            index = key % self.capacity

        current = self.buckets[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1
        

    def remove(self, key):
        index = key % self.capacity

        current = self.buckets[index]
        prev = None 

        while current: 
            if current.key == key:
                if prev is None:
                    self.buckets[index] = current.next
                else:
                    prev.next = current.next
                return
            
            prev = current
            current = current.next