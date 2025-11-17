from collections import defaultdict

def group_anagrams(words):
    groups=defaultdict(list)
    for w in words:
        key=''.join(sorted(w))
        groups[key].append(w)
    return list(groups.values())

words=["eat", "tea", "ate", "tan"]
result=group_anagrams(words)
print(result)