"""

3->7->5->12->None

"""


class SinglyListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None


a = SinglyListNode(3)
b = SinglyListNode(7)
c = SinglyListNode(5)
d = SinglyListNode(12)

a.next = b
b.next = c
c.next = d


print(a.next)
print(b)
print(b.next)
print(c)


def iterate(head):
    # goes through the linkedlist and whenever it sees next pointer as None, it stops
    current = head

    while current != None:
        print(current.value)
        current = current.next


iterate(a)
