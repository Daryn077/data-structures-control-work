# # 1нұсқа
# # 1.2 
# class Node:
#     def _init_(self, val):
#         self.val = val 
#         self.next = None

# a = None(1)
# a.next = Node(2)
# a.next.next = Node(3)
# a.next.next.next = Node(2)
# a.next.next.next.next = Node(4)

# def remove_val
        

# 1.1
words = ["нан", "ар", "кек", "мұң"]

hash_table = {}  

for w in words:
    key = "".join(sorted(w))  
    if key not in hash_table:
        hash_table[key] = []
    hash_table[key].append(w)

result = list(hash_table.values())

print(result)


















































#  class Node:
# #     def __init__(self, val):
# #         self.val = val
# #         self.next = None

# # a = Node(1)
# # a.next = Node(2)
# # a.next.next = Node(3)
# # a.next.next.next = Node(2)
# # a.next.next.next.next = Node(4)