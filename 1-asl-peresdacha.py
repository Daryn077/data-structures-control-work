#4 

first = [1, 2, 2, 3, 3, 3]
second = [1, 1, 2, 3, 3, 3]
k = 3

a = 3
b = 3

first_count = {}
second_count = {}

both = 0

for i in first:
    if i in first_count:
        first_count[i] = first_count[i] + 1
    else:
        first_count[i] = 1
print(first_count)
    
for i in second:
    if i in second_count:
        second_count[i] = second_count[i] + 1
    else:
        second_count[i] = 1
print(second_count)


for key, value in first_count.items():
    if value == a:
        
        for keyy, valuee in second_count.items():
            if valuee == b: 
                both = min(a, b) * k + abs(a - b)     
                
print(both)




#2

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        
h = Node(1)
h.next = Node(3)
h.next.next = Node(5)
h.next.next.next = Node(8)
h.next.next.next.next = Node(11)

while h:
    if h.next.val - h.val != k:
        print(False)
        break
    h = h.next
        

while h:
    print(h.val)
    h = h.next
print(True)
    