# Python 2.7
# Print the part of the array of numbers
# Test cases
    # 'abc45,67,ldkshwi5'

def PrintNUmericPart(input):
    return filter(str.isdigit, input)


input = 'abc45,67,ldkshwi5'
print(PrintNUmericPart(input))