#1 
sun = [10, 5, 7, 12, 3, 8]
m = 5

counts = {}

i = 0
while i < len(sun):
    a = sun[i] % m

    if a in counts:
        counts[a] += 1
    else:
        counts[a] = 1

    i += 1


    print(counts)


#2
# class Node:
#      def __init__(self, value, next=None):
#          self.value = value
#         self.next = next





