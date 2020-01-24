def pairwise(t):
    res = list(zip(t, t[1:] + t[:1]))
    return res


t = [1,4,5]
print(pairwise(t))
