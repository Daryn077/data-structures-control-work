# 4 нұсқа
# 1 esep
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

l1 = Node(1)
l1.next = Node(3)
l1.next.next = Node(3)
l1.next.next.next = Node(5)
l1.next.next.next.next = Node(6)
l1.next.next.next.next.next = Node(7)

l2 = Node(2)
l2.next = Node(3)
l2.next.next = Node(4)
l2.next.next.next = Node(5)
l2.next.next.next.next = Node(7)
l2.next.next.next.next.next = Node(8)

res = {}




# 2 esep
# class Node:
#     def __init__(self, value, next = None):
#         self.value = value
#         self.next = next
        
# head = Node(1)
# head.next = Node(3)
# head.next.next = Node(5)
# head.next.next.next = Node(7)
# head.next.next.next.next = Node(9)

# def is_arifmetic(head):
#     if head is None or head.next is None:
#         return True
    
#     diff = head.next.value - head.value
    
#     current = head.next
#     while current.next:
#         if current.next.value - current.value != diff:
#             return False
#         current = current.next
        
#     return True

# print(is_arifmetic(head))