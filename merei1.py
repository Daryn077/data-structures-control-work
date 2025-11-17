# # 1 тапсырмма
words = ["алма", "шай", "шоколад", "сок", "шай", "алма"]

i = 0
groups = []

while i < words.__len__():
    w = words[i]
    a = list(w)
    x = 0
    while x < a.__len__():
        y = 0
        while y < a.__len__() - 1:
            if a[y] > a[y+1]:
                t = a[y]
                a[y] = a[y+1]
                a[y+1] = t
            y += 1
        x += 1
    s = "".join(a)

    j = 0
    f = 0
    while j < groups.__len__():
        if groups[j][0] == s:
            groups[j].append(w)
            f = 1
            break
        j += 1

    if f == 0:
        groups.append([s, w])
    i += 1

print(groups)




# # 2 тапсырма
# class N:
#     def __init__(self, v):
#         self.v = v
#         self.n = None

# a = N(1)
# b = N(2)
# c = N(3)
# d = N(2)
# e = N(4)

# a.n = b
# b.n = c
# c.n = d
# d.n = e

# tgt = 2
# h = a

# while h != None and h.v == tgt:
#     h = h.n

# p = h
# while p != None and p.n != None:
#     if p.n.v == tgt:
#         p.n = p.n.n
#     else:
#         p = p.n

# q = h
# while q != None:
#     print(q.v, end=" ")
#     q = q.n

