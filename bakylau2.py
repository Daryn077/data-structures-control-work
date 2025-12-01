# from collections import deque
# def is (x:int) bool 
#     if x<=1:
#         return False
#     if x<=3:
#         return True 
#     if x % 2 == 0:
#         return False 
#     


# 2 тапсырма
def inorder_iter(root):
    stack = []
    cur = root
    res = []
    even_sum = 0

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        res.append(cur.val)
        if cur.val % 2 == 0:
            even_sum += cur.val

        cur = cur.right

    return res, even_sum
root = Node(4,
    Node(2, Node(1),
       Node(3)),
    Node(6))

print(inorder_iter(root))

