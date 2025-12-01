# # 1 3нуска
# nums=[12, 21, 30, 111, 102, 40]

# groups = {}

# for x in nums:
#     s = sum(int(d) for d in str(x)) 
#     if s not in groups:
#         groups[s] = []
#     groups[s].append(x)

# print(groups)



# 2 шы бакылау 2нуска

# 1
from collections import deque 

graph = (
    0: 1
    1: 2
    2: 3
    3: 4
    4: 5
    5: 6
)

q = deque ([1])

# 2
def count_preorder(root, k):
    st, c = [root], 0 
    

