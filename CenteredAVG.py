def CenteredAvg(input):
    sorted_input = sorted(input)
    if len(input) >= 3:
        sorted_input.remove(sorted_input[0])
        sorted_input.remove(sorted_input[-1])
        result = sum(sorted_input) / len(sorted_input)
    else:
        result = "input length must be longer than 3 elements"
    return result



input = [1, 1]
print(CenteredAvg(input))
