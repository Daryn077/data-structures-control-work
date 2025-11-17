# 5 нұсқа
# 2 tapsyrma
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

pos = 1
res = 1

curr = head
while curr:
    if pos % 2 == 1:
        res *= curr.value
    curr = curr.next
    pos += 1
           
print(res)

# 1 tapsyrma
s = [12, 36, 45, 555]

res = {}

for num in s:
    summ = 0
    sign = 1
    for ch in str(num):
        summ += sign * int(ch)
        sign *= -1

    if res.get(summ) is None:
        res[summ] =  
    else:
        res[summ] = 
        

print(res)

    
    