# Python 2.7
# Most recurring element in a list
# Test cases
    # arr = [-5, -5, -3, -4, 0, -1]
    # arr = [1, -1, 1, -5, -5]
    # arr = [-5, -4, -3, -4, 0, -5]

# Solution 1
arr = [-5, -5, -5, -4, 0, -1]
print max(arr, key=arr.count)

# Solution 2
def mostRecurring(list):
    list = input("Please enter a list: ")
    n_list = []
    element = 0
    max_value = ""
    for n in list:
        if n not in n_list:
            n_list.append(n)
        else:
            continue
    for x in n_list:
        counter = 0
        for j in list:
            if j == x:
                counter += 1
        if counter > element:
            element = counter
            max_value = x
    return max_value

print(mostRecurring(list))






# Solution 3
def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num


List = [2, 1, 2, 2, 1, 3]
print(most_frequent(List))