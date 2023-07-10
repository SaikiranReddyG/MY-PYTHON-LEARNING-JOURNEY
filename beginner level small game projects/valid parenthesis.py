def isvalid(s):
    global char
    stack = []
    mapping = {')':"(", '}':'{', ']':'['}

    """iterate through each charecter in the input string"""
    for char in s:
        if char in mapping:  # if the charecter is a closing bracket
            # pop the top element from the stack or use a place holder
            top_element = stack.pop() if stack else '#'
            """if the popped element is the coressponding opening bracket"""
            if mapping[char] != top_element:
                return False

        else:
            stack.append(char)  # if the charecter is an opening bracket push it to the stack

    return not stack


# input the string from the user
input_string = input('enter the string here')
is_valid = isvalid(input_string)

if is_valid:
    print('the output is valid')
else:
    print('the output is not valid')



