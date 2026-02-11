'''
- key: estes são os dados de entrada (ou, mais comumente, o valor inteiro do hash derivado da chave original usando uma função 
hash) que você deseja armazenar ou recuperar na tabela hash.
- % (Modulo Operator): Este operador retorna o resto da divisão da chave por self.capacity.
- self.capacity: Refere-se ao tamanho atual (número de slots ou "buckets" disponíveis) do array interno da tabela hash.
- index:  resultado da operação é um inteiro que está dentro do intervalo (ou "range") [0, self.capacity - 1], que corresponde 
diretamente a um índice válido no array.
- E foi utilizado listas encadeadas junto com tudo isso para resolver este problema.
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