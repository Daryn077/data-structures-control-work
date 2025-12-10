#2 nuska 1 esep
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

    # Графтың байланыстылығын BFS нәтижесімен тексеру
    if len(visited) == len(graph):
        print("Граф байланысты")
    else:
        print("Граф байланысты емес")

    # ✔ ДҰРЫС XOR — тек BFS барған төбелерден
    xor_value = 0
    for v, _ in visited.items():     # ← мұғалім айтқан дұрыс жол
        degree = len(graph[v])
        xor_value = xor_value ^ degree

    print("BFS барған төбелердің XOR:", xor_value)


bfs(graph, 1)
    
    
#2 esep
# class BinaryTree:
#     def __init__(self, val, left = None , right = None):
#         self.val = val
#         self.left = left 
#         self.right = right 

# root = BinaryTree(val = 10)
# root.left = BinaryTree(val = 5)
# root.right = BinaryTree(val=20)
# root.right.left = BinaryTree(val=15)
# root.right.right = BinaryTree(val=30)

# k = 12

# stack = []
# res = []
# count = 0

# if root is not None:
#     stack.append(root)


# while len(stack) > 0:
#     node = stack.pop()      
#     res.append(node.val) 
#     if node.val > k:
#         count += 1

#     if node.right is not None:
#         stack.append(node.right)

#     if node.left is not None:
#         stack.append(node.left)

# print(res , count)

