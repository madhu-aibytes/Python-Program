from collections import defaultdict
d=defaultdict(list)
l=["rat","cat","apple","car","banana"]
for i in l:
    d[len(i)].append(i)
print(list(d.values()))
    
