# Python version: 2.7
# Question_2: Function to give the minimun number of letters to identify strings
 # Lowercase and uppercase letters are considered as different
 # Input string must not contains spaces

# Test values used:
  # strings = privalia,veepee,venteprivate
  # strings = aacaa,aacba,aacca
  # strings = abcd,abdc,abfg
  # strings = ab,ab
  # strings = Ab,AB
  # strings = carlos,Antonio,angel
  # strings = carlos,antonio,angel
  # strings = abc,abc,cdf
  # strings = cdf,abc,abc

def MinNumberLetters():
    word_list = []
    chards_list = []
    strings = raw_input("Please enter a list of strings(seperated by a comma): ")
    word_list = strings.split(",") # split list of strings by comma
    for word in word_list: # splits strings in characters
        chards_list.append(list(word))

    eq = [] # list of character matches
    b = ""  # first value to compare
    for index1, item in enumerate(chards_list): # iterate over list of list of characters
        for index2, char in enumerate(item): # iterate over list of characters
            if char != b: # check is char is not equal to firs value
                b = char # assing new value to compare
                break
            else:
                eq.append(char) # append character to list of character matches
                if index2 == len(chards_list[index1 - 1]) - 1: # check if the character is the penultimate
                    break
                else:
                    b = chards_list[index1 - 1][index2 + 1] # assing new value to compare
                pass
    if len(eq) >= len(max(chards_list,key=len)): # check if strings provided are equal
        print "Strings cannot be identify, string are equal"
    else:
        print "Minimun number of letters to identify strings is ", len(eq) + 1

# Function execution
MinNumberLetters()








