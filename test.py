def function(l, n):
    new = []
    test = ['']
    for n in l:
        if len(test) < 2:
            test.append([n])
            if len(test) == 2:
                new.append(test)
                test = ""
    return new


l = ['1', '2', '1', '2', '3']
n = 2
print(function(l, n))
