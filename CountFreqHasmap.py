# Python 2.7
# Count the frequency of words from the list and store the results in a hash map
# Test cases
    # ['hola', 'tete', 'hola', 'adios', 'tete', 'casa']

# Solution 1
def CountFreqHasmap(input):
    keys = []
    values = []
    for word in input:
        if word not in keys:
            keys.append(word)
        else:
            continue
    for n in keys:
        counter = 0
        for word in input:
            if word == n:
                counter += 1
                values.append(counter)
            else:
                continue
    dict = {k: v for k, v in zip(keys, values)}
    return dict

input = ['hola', 'tete', 'hola', 'adios', 'tete', 'casa']
print(CountFreqHasmap(input))

# Solution 2
def CountFreqHasmap(input):
    keys = []
    values = []
    for word in input:
        if word not in keys:
            keys.append(word)
            values.append(input.count(word))
        else:
            continue
    dict = {k: v for k, v in zip(keys, values)}
    return dict

input = ['hola', 'tete', 'hola', 'adios', 'tete', 'casa']
print(CountFreqHasmap(input))
