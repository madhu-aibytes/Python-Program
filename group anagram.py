from collections import defaultdict
a=defaultdict(list)
l=["eat","tea","ate","mat","bat","cat"]
for i in l:
    key=''.join(sorted(i))
    a[key].append(i)
print(list(a.values()))