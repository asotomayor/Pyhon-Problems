# Python 2.7
# Count the number of unique words in a sequence?
# Test cases
    # ['one', 'two', 'two']

def CountUniqueWords(input):
    unique = set(input)
    return len(unique)

input = ['one', 'two', 'two']
print(CountUniqueWords(input))
