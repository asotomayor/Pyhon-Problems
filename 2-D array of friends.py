# Python 2.7
# You have a 2-D array of friends like [[A,B],[A,C],[B,D],[B,C],[R,M], [S],[P], [A]]
# Write a function that creates a dictionary of how many friends each person has. People can have 0 to many friends.
# However, there won't be repeat relationships like [A,B] and [B,A] and neither will there be more than 2 people in a relationship .
# Test cases
    # [['A','B'],['A','C'],['B','D'],['B','C'],['R','M'],['S'],['P'],['A']]
    #

def DictionaryFriends(input):
    dic = {}
    for n in input:
        if len(n) > 1:
            for x in n:
                if x not in dic.keys():
                    dic[x] = 1
                else:
                    dic[x] += 1
        else:
            if n[0] not in dic.keys():
                dic[n[0]] = 0
    return dic

input = [['A','B'],['A','C'],['B','D'],['B','C'],['R','M'],['S'],['P'],['A']]
print(DictionaryFriends(input))

# Solution 2
items=[['A','B'],['A','C'],['B','D'],['B','C'],['R','M'], ['S'],['P'], ['A']]
result=dict()
for item in items:
    if item[0] not in result.keys():
        result[item[0]]=len(item)-1
    elif item[0] in result.keys():
        result[item[0]]+=len(item)-1

print(result)