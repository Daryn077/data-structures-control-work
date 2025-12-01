def simple_dfs_count(graph, start, V):
    stack = [start]
    visited = set()
    count = 0

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            if node == V and node % 2 == 0:
                count += 1
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return count

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

start = 1
V = 4  
print(simple_dfs_count(graph, start, V))
