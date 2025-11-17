# 4 нұсқа  

def weighted_intersection(list1, list2, k):
   
    freq1 = {}
    freq2 = {}

    for x in list1:
        freq1[x] = freq1.get(x, 0) + 1

    for x in list2:
        freq2[x] = freq2.get(x, 0) + 1

    
    all_nums = set(list1) | set(list2)

    result = {}

    for num in all_nums:
        a = freq1.get(num, 0)
        b = freq2.get(num, 0)

        # Егер екі тізімде де кездессе
        if a > 0 and b > 0:
            result[num] = min(a, b) * k + abs(a - b)
        else:
            # Тек бір тізімде болса — 0
            result[num] = 0

    return result


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_arithmetic_progression(head):
    
    arr = []
    curr = head

    while curr:
        arr.append(curr.value)
        curr = curr.next

    
    if len(arr) < 2:
        return True

    
    d = arr[1] - arr[0]

    
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] != d:
            return False

    return True




l1 = [1, 2, 2, 3, 5]
l2 = [2, 2, 2, 3, 4]
k = 3

print("Салмақталған қиылысу нәтижесі:")
print(weighted_intersection(l1, l2, k))


head = Node(2)
head.next = Node(5)
head.next.next = Node(8)
head.next.next.next = Node(11)

print("\nТізім арифметикалық прогрессия ма?")
print(is_arithmetic_progression(head))
