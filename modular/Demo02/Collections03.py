from collections import Counter
c = Counter()
for i in "dsfadsfasdfasdf":
    c[i] = c[i]+1
print(c)