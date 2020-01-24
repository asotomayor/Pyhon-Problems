# Python 2.7
# Median in a list
# Test cases
    # list = [10, 20, 4, 45, 99]
    # list = [-5, -5, -3, -4, 0, -1]
    # list = [-500, -50, -3,5, 1000]

# Solution 1
def median(list):
    #list = input("Please enter a list: ")
    sorted_List = sorted(list)
    len_list = len(list)
    index = (len_list - 1) // 2

    if (len_list % 2):
        return sorted_List[index]
    else:
        return (sorted_List[index] + sorted_List[index + 1])/2.0
list = [10, 20, 4, 45, 99]
print (median(list))

# Solution 2
def median(list):
    #list = input("please enter a list: ")
    sorted_list = sorted(list)
    index = (len(list) - 1) / 2
    if len(list) % 2 != 0:
        x = list[index]
    else:
        x = (list[index] + list[index+1]) / 2.0
    return x

list = [10, 20, 4, 45, 99]
print (median(list))