def findDuplicates(input):
    dup = []
    non_dup =[]
    for n in input:
        if n not in dup:
            non_dup.append(n)
        else:
            dup.append(n)
    return dup

# test
input = ['1', '2', '2', '3', '4', '3']
print(findDuplicates(input))