# Python 2.7
# Flatten list of list
# 1. The loop way
def flattenList():
    list_of_lists = [range(4), range(7)]
    flattened_list = []
    for x in list_of_lists:
        for y in x:
            flattened_list.append(y)
    return flattened_list

print flattenList()

# 2. List comprehension way
def flattenList():
    list_of_lists = [range(4), range(7)]
    #flatten the lists
    flattened_list = [y for x in list_of_lists for y in x]
    return flattened_list
print flattenList()