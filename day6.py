import liwei.advent as lt
from collections import Counter

counts = [Counter(col) for col in zip(*lt.Input(6).read().split())]
# print(lt.Input(6))
# print(lt.Input(6).read())
# print(lt.Input(6).read().split())


answer1 = ''.join(e.most_common()[0][0] for e in counts)
print(answer1)

answer2 = ''.join(e.most_common()[-1][0] for e in counts)
print(answer2)


