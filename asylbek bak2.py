# 2 нуска
# 2 тапсырма
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

        
# a = Node(5)
# a.left = Node(3)
# a.right = Node(8)
# a.left.left = Node(2)
# a.right.left = Node(6)
# a.right.right = Node(10)


# def preorder(a, k):
#     if not a:
#         return 0

#     stack = [a]
#     count = 0

#     while stack:
#         node = stack.pop()
#         if node.val > k:
#             count += 1
#         if node.right:
#             stack.append(node.right)
#         if node.left:
#             stack.append(node.left)
#     return count


# k = 5
# print(" мәні > k:",preorder(a, k))


#1 тапсырма
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2],
    5: [3, 6],
    6: [5]
}

def bfs(graph, start):
    queue = [start]
    visited = {start: True}
    res = []

    while queue:
        current = queue.pop(0)
        res.append(current)

        for neigh in graph[current]:
            if neigh not in visited:
                visited[neigh] = True
                queue.append(neigh)

    print("Порядок BFS:", res)

    if len(visited) == len(graph):
        print("Граф байланысты")
    else:
        print("Граф байланысты емес")

    xor_value = 0
    for v, _ in visited.items():     
        degree = len(graph[v])
        xor_value = xor_value ^ degree

    print("BFS барған төбелердің XOR:", xor_value)


bfs(graph,1)











    



















        
    