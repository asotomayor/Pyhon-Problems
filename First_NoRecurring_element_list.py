# Python 2.7
# First no Recurring element in a list

# Test cases
    # arr = [-5, -5, -3, -4, 0, -1]
    # arr = ['aab', 'aab', 'test']
    # arr = [-5, -4, -3, -4, 0, -5]

# Solution 1
arr = ['1', '2', '1']
print min(arr, key=arr.count)

# Solution 2
def firstNoRecurring(list):
    #list = input("Please enter a list of elements: ")
    n_list =[]
    r_list = []
    element = ""
    for n in list:
        if n not in n_list:
            n_list.append(n)
        else:
            r_list.append(n)
    for x in n_list:
        if x in r_list:
            continue
        else:
            element = x
            break
    return(element)

list = ['1', '2', '1']
print(firstNoRecurring(list))
