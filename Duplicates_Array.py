# Python 2.7
# Find duplicates in array
# Test cases
    # arr = ['abcdeabcc']
    #
def FindDuplicatesArr(input):
    uniques = []
    duplicates = []
    for n in input:
        if n not in uniques:
            uniques.append(n)
        else:
            duplicates.append(n)
    return duplicates

input = ['aa', 'ab', 'cc', 'aa', 'ab']
print(FindDuplicatesArr(input))