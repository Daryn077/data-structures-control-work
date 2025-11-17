# #1

# summ = [10, 22, 30, 44, 50]



# for number in summ:
#     plus = 0
    
#     for i in number:
#         plus += i
        
#     number = plus

# print(summ)




# #2

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
    
