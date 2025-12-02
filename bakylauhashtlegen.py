#5 nuska #1 esep
arr = [101, 333, 2342, 532, 61, 92091, 1380, 1938]

diction = {}

for i in arr:
    summ = 0
    a = i
    flag = False
    for j in range(len(str(i))):
        k = a%10
        if flag:
            summ += k
        else:
            summ -= k
        a = a//10
        flag = not flag

    if diction.get(summ, False):
        diction[summ] += [i]
    else:
        diction[summ] = [i]
print(diction)








#2 esep 
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.next.next = Node(5)
root.next.next.next.next.next = Node(6)
root.next.next.next.next.next.next = Node(7)

mul = 1
count = 1
while root:
    if count % 2 != 0:
        mul *= root.val
    root = root.next
    count += 1

print(mul)








    

