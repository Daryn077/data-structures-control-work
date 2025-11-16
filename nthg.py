# class Node:
#     def __init__(self, value, next = None):
#         self.value = value
#         self.next = next
        
# head = Node(value = 1)
# head.next = Node(1)
# head.next.next = Node(3)
# head.next.next.next = Node(6)
# head.next.next.next.next = Node(5)


# slow = head.next
# fast = head.next.next

# while curr != None:
#     print(curr.value, end = ' ')
#     curr = curr.next

# print("\n")
        
# slow = head.next
# fast = head.next.next
# n = 4
# c = 1
# while n > 0:
#     if c == n:
#         prev.next = curr.next
#         break
    
#     prev = curr
#     curr = curr.next
#     c += 1
    
    
    
    
    
    
# n = [1, 1, 1, 3, 7, 8, 8, 9]

# count = {}

# for i in n:
#     if count.get(i) is None:
#         count[i] = 1
#     else:
#         count[i] += 1

# for key, value in count.items():
#     if value > 1:
#         while value > 1:
#             n.remove(key)
#             value -= 1
        
# print(n)
    
    
    
    
    
    
sums = []

for