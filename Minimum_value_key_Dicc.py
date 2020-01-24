# Python 2.7
# Minimum value_key in a dictionary
# Test cases
    # {'Gfg': 11, 'for': 2, 'CS': 11, 'geeks': 8, 'nerd': 2}
    # {'country': 11, 'state': 2, 'city': 11, 'street': 8, 'number': 2}

# Solution 1
def MinKeyValue():
    dic = {'country': 11, 'state': 2, 'city': 11, 'street': 8, 'number': 2}
    temp = min(dic.values())
    res = [key for key in dic if dic[key] == temp]
    return res

print(MinKeyValue())

# Solution 2
def MinKeyValue():
    dic = {'country': 11, 'state': 2, 'city': 11, 'street': 8, 'number': 2}
    dic_values = []
    min_keys = []
    test = ""
    for key, value in dic.iteritems():
        if value < test:
            del min_keys[:]
            min_keys.append(key)
            test = value
        elif value == test:
            min_keys.append(key)
            test = value
        else:
            continue
    return min_keys

print(MinKeyValue())
