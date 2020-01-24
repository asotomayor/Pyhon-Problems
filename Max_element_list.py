# Python 2.7
# Maximun element in a list
# Test cases
    # list = [10, 20, 4, 45, 99]
    # list = [-5, -5, -3, -4, 0, -1]
    # list = [-500, -50, -3,5, 1000]

# Solution 1
print("Largest element is:", max(list1))

# Solution 2
def MaxElementList(list):
    list = input("Please enter a list: ")
    max_element = list[0]
    for n in list:
        if n > max_element:
            max_element = n
        else:
            continue
    return max_element
print(MaxElementList(list))
