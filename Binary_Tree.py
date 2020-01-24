# Class to define a node
# structure of the tree
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Function to convert ternary
# expression to a Binary tree
# It returns the root node
# of the tree
def convert_expression(expression, i):
    if i >= len(expression):
        return None

    # Create a new node object
    # for the expression at
    # ith index
    root = Node(expression[i])

    i += 1

    # if current character of
    # ternary expression is '?'
    # then we add next character
    # as a left child of
    # current node
    if (i < len(expression) and
            expression[i] is "?"):
        root.left = convert_expression(expression, i + 1)

        # else we have to add it
    # as a right child of
    # current node expression[0] == ':'
    elif i < len(expression):
        root.right = convert_expression(expression, i + 1)
    return root


# Function to print the tree
# in a pre-order traversal pattern
def print_tree(root):
    if not root:
        return
        print(root.data, end==' ')
    print_tree(root.left)
    print_tree(root.right)


# Driver Code
if __name__ == "__main__":
    string_expression = "a?b?c:d:e"
    root_node = convert_expression(string_expression, 0)
    print_tree(root_node)

# This code is contributed
# by Kanav Malhotra
# test
s = 'a?b:c'
i= 3
print(convert_expression(s, i))