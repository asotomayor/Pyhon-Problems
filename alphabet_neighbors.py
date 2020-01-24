# Python 2.7
# You have a 2-D array of friends like [[A,B],[A,C],[B,D],[B,C],[R,M], [S],[P], [A]]
# Write a function that creates a dictionary of how many friends each person has. People can have 0 to many friends.
# However, there won't be repeat relationships like [A,B] and [B,A] and neither will there be more than 2 people in a relationship .
# Test cases
    # [['A'],['A','B'],['A','C'],['B','D'],['C','A']]
    # [['A','B'],['A','C'],['B','D'],['B','C'],['R','M'],['S'],['P'],['A']]

def alphabet_highest_neighbors(input):
    dic = {}
    neighbords = 0
    alphabet = ""
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
    print dic

    for key, value in dic.items():
        if value > neighbords:
            neighbords = value
            alphabet = key
        else:
            continue
    print alphabet


input = [['A','B'],['A','C'],['B','D'],['B','C'],['R','M'],['S'],['P'],['A']]
print(alphabet_highest_neighbors(input))