def palindrom(s):
    chars = list(s)
    rev_chards = []
    for char in reversed(chars):
        rev_chards.append(char)
    if chars == rev_chards:
        return True
    else:
        return False


# test
s = 'abaa'
print(palindrom(s))
