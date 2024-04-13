from itertools import combinations_with_replacement

s = input()
substrings = {s[i: j + 1] for i, j in combinations_with_replacement(range(len(s)), r=2)}
print(len(substrings))

