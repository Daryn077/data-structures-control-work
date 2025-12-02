#3 нуска
# 1-тапсырма 
# arr = [100, 3, 23, 5, 61, 92, 10, 19]
# dict = {}
# for i in arr:
#     sum = 0
#     a = i
#     for j in range(len(str(i))):
#         k = a%10
#         sum += k
#         a = a//10

#     if dict.get(sum, False):
#         dict[sum] += [i]
#     else:
#         dict[sum] = [i]
# print(dict)



# 2
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(2)
a.next.next.next.next = Node(4)

slow = fast = a
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    
    while fast:
        slow = slow.next
        if fast.next:
            fast = fast.next.next
        else:
            break
    return slow.val
print((a))







