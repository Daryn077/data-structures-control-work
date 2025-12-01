graph = {
    0: [1,2],
    1: [0,3],
    2: [0],
    3: [1]
}

# 2
def bfs(start, graph):
    
    queue = [start]
    visited = set()
    
    while queue:
        