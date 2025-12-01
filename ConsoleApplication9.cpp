// ConsoleApplication9.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#1нуска
# 1) BFS және қарапайым сандарды санау


def bfs(adj, start) :
    visited = set()
    order = []
    q = deque([start])
    visited.add(start)

    while q:
u = q.popleft()
order.append(u)
for v in adj.get(u, []) :
    if v not in visited :
visited.add(v)
q.append(v)
return order


def is_prime(n) :
    if n <= 1 :
        return False
        if n <= 3 :
            return True
            if n % 2 == 0 :
                return False
                i = 3
                while i* i <= n :
                    if n% i == 0 :
                        return False
                        i += 2
                        return True


                        # Граф(есептегі сияқты)
                        adj = {
                            1: [2, 3] ,
                            2 : [4] ,
                            3 : [4, 5] ,
                            4 : [6] ,
                            5 : [6, 7] ,
                            6 : [] ,
                            7 : []
                    }

                        start = 1
                        order = bfs(adj, start)
                        prime_count = sum(1 for x in order if is_prime(x))

                        print("BFS order:", order)
                        print("Prime numbers encountered:", prime_count)



                        # 2) Итеративті In - Order обход және жұп сандар қосындысы


                        class Node :
                        def __init__(self, val) :
                        self.val = val
                        self.left = None
                        self.right = None


                        def inorder_iterative(root) :
                        stack = []
                        curr = root
                        order = []
                        even_sum = 0

                        while curr or stack:
while curr :
    stack.append(curr)
    curr = curr.left

    curr = stack.pop()
    order.append(curr.val)
    if curr.val % 2 == 0:
even_sum += curr.val

curr = curr.right

return order, even_sum


# Мысал ағаш(есепке көрсету үшін)
#       4
#     /   \
#    2     6
#   / \   / \
#  1  3  5  7

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

order2, ev_sum = inorder_iterative(root)

print("Iterative in-order:", order2)
print("Sum of even values:", ev_sum)