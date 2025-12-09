# 4 нұсқа
# 2 тапсырма
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.left = Node(6)
a.right.right = Node(7)

K = 2

queue = [(a, 0)]    
max_val = None

while queue:
    node, lvl = queue[0]
    queue = queue[1:]    

    if lvl == K:
        if max_val is None or node.val > max_val:
            max_val = node.val

    if node.left:
        queue.append((node.left, lvl + 1))
    if node.right:
        queue.append((node.right, lvl + 1))

print(max_val)




# 1 тапсырма
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

in_degree = {u: 0 for u in graph}
for u in graph:
    for v in graph[u]:
        in_degree[v] = in_degree.get(v, 0) + 1

queue = [u for u in in_degree if in_degree[u] == 0]
top_order = []

while queue:
    u = queue[0]
    queue = queue[1:]
    top_order.append(u)
    for v in graph.get(u, []):
        in_degree[v] -= 1
        if in_degree[v] == 0:
            queue.append(v)

print(top_order)
print(sum(top_order))
