#1

class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
s = Node(0, Node(1, Node(2), Node(3)), Node(4, Node(5, Node(6), Node(7)), Node(8)))

stack = [s]

visited = []

while stack:
    cur = visited.pop()
    for i in cur:
        if cur[i] in visited:
            visited.append(cur[stack[s]])
            
            
            
            
            
            
            
            
            
#2


class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
tree = Node(0, Node(1, Node(2), Node(3)), Node(4, Node(5, Node(6), Node(7)), Node(8)))

stack = [tree]


while stack:
    current = stack.pop(-1)
    
    if current.right:
        stack.append(current.right)
    
    if current.left:
        stack.append(current.left)
    


            