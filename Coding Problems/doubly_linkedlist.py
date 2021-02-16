class DoublyListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


a = DoublyListNode(3)
b = DoublyListNode(7)
c = DoublyListNode(5)
d = DoublyListNode(12)

a.next = b
b.next = c
c.next = d
c.prev = b
b.prev = a

print(a.next.prev.value)  # 3
print(b)
print(b.next)
print(c)
print(b.prev)
print(a)
print(c.prev)
print(b)
print(c.prev.prev.value)  # 3
print(c.prev.prev.prev)  # None
