# 2
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# l1 = Node(1)
# l1.next = Node(3)
# l1.next.next = Node(5)
# l1.next.next.next = Node(6)
# l1.next.next.next.next = Node(7)
# l1.next.next.next.next.next = Node(8)

# l2 = Node(2)
# l2.next = Node(4)
# l2.next.next = Node(9)
# l2.next.next.next = Node(10)

# dummy = Node(0)
# current = dummy

# while l1 is not None and l2 is not None:
#     if l1.value < l2.value:
#         current.next = l1
#         l1 = l1.next
#     else:
#         current.next = l2
#         l2 = l2.next
#     current = current.next

# if l1 is not None:
#     current.next = l1
# else:
#     current.next = l2

# merged = dummy.next

# p = merged
# while p is not None:
#     print(p.value, end=" ")
#     p = p.next


# 3
# class Node:
#     def __init__(self, value, next = None):
#         self.value = value
#         self.next = next
        
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)
# head.next.next.next.next.next = Node(6)

# slow = head
# fast = head
# prev = None

# while fast and fast.next:
#     prev = slow
#     slow = slow.next
#     fast = fast.next.next
    
# prev.next = None

# p = head
# while p:
#     print(p.value, end = ' ')
#     p = p.next
# print("\n")
# p = slow
# while p:
#     print(p.value, end = " ")
#     p = p.next


# 4
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)
# head.next.next.next.next.next = Node(6)

# slow = head
# fast = head
# while fast and fast.next:
#     slow = slow.next
#     fast = fast.next.next
    
# prev = None
# curr = slow
# while curr:
#     nxt = curr.next
#     curr.next = prev
#     prev = curr
#     curr = nxt
    
# left = head
# right = prev

# is_palindrome = True
# while right:
#     if left.value != right.value:
#         is_palindrome = False
#         break
#     left = left.next
#     right = right.next
    
# print(is_palindrome)


5
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

m = 2
n = 5

dummy = Node(0, head)
prev = dummy

for _ in range(m-1):
    prev = prev.next
    
start = prev.next
then = start.next

for _ in range(n - m):
    start.next = then.next
    then.next = prev.next
    prev.next = then
    then = start.next
    
head = dummy.next

curr = head
while curr:
    print(curr.value, end = " ")
    curr = curr.next
    