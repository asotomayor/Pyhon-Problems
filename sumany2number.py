# Given a number and a array. Python code to find sum of any 2 numbers in a list is equal to a given number.

def findPairs(k, lst):
    n = len(lst)
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            e1 = lst[i]
            e2 = lst[j]
            if e1 + e2 == k:
                count += 2
    return count

k = 16
lst = [1,4,45,6,10,-8]
print(findPairs(k, lst))