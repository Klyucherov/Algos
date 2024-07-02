from collections import Counter


def solutionM(txt):
    count = Counter(txt)
    sorted_data = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    return  ''.join(key * count for key, count in sorted_data)


txt = 'tree'
txt2 = 'ztwidhfk'
 
print(solutionM(txt))
print(solutionM(txt2))
