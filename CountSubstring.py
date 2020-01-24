# Count the number of times a substring appear in a string

def countsub(s, p):
    n = s.count(p)
    return n

s = 'antoniosotomayorsola'
p = 'antonio'

print(countsub(s,p))