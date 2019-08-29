# Python version: 2.7
# Question_1: Function to print numbers from 1 to x
  # When number is multiple of 3 then print "Vee"
  # When number is multiple of 5 then print "pee"
  # when number is multiple of 3 and 5 then print "Veepee"

# Test values used: 0, 10, 15, 100, -100, 0,8, 1200

def PrintNumber():
    x = input("Please enter a positive integer number: ")
    numbers = []
    if (x < 1) | (isinstance(x, int) == False): # check if input number is a postive integer
        print "input number must be a positive integer number"
    else:
        for n in range(1,x,1):
            if (n % 3 == 0) & (n % 5 == 0): # check if n is multiple of 3 and 5
                number = "Veepee"
                numbers.append(number)
            elif (n % 3 == 0) & (n % 5 != 0): # check if n is multiple of 3 but not 5
                number = "Vee"
                numbers.append(number)
            elif (n % 3 != 0) & (n % 5 == 0): # check if n is multiple of 5 but not 3
                number = "pee"
                numbers.append(number)
            else: # n is not multiple of 3 and 5
                number = n
                numbers.append(number)
    print numbers

# Function execution
PrintNumber()



