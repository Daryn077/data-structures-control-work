# 1
nums=[12, 21, 30, 111, 102, 40]

groups = {}

for x in nums:
    s = sum(int(d) for d in str(x)) 
    if s not in groups:
        groups[s] = []
    groups[s].append(x)

print(groups)
