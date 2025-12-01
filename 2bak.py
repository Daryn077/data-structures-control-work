# 2 тапсырма
class node




# 1 тапсырма

from collections import deque

graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}

def bfs_level_max(graph, start, k):
    q = deque()
    q.append((start, 0))
    visited = set([start])

    level_nodes = []

    while q:
        node, level = q.popleft()

        if level == k:
            level_nodes.append(node)

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append((nei, level + 1))

    if level_nodes:
        return max(level_nodes)
    return None


k = 1
print(k, "деңгейдегі ең үлкен мән:", bfs_level_max(graph, 0, k))
