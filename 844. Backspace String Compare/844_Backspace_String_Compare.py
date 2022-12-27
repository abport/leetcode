def backspaceCompare(s, t):
    # Define a helper function to apply the backspace operation to a given string
    def get_final_string(string):
        # Initialize an empty stack to store the characters we want to keep
        stack = []
        # Iterate over the characters in the string
        for c in string:
            # If the character is a backspace character, pop the last character from the stack if the stack is not empty
            if c == '#':
                if stack:
                    stack.pop()
            # If the character is not a backspace character, add it to the stack
            else:
                stack.append(c)
        # Join the characters in the stack and return the resulting string
        return "".join(stack)

    # Compare the final strings of s and t and return the result
    return get_final_string(s) == get_final_string(t)
