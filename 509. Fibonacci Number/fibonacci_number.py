def isValid(s: str) -> bool:
    # Create an empty stack to keep track of open brackets
    stack = []
    
    # Iterate through each character in the string
    for c in s:
        # If the character is an open bracket, push it onto the stack
        if c in ('(', '[', '{'):
            stack.append(c)
        # If the character is a close bracket, 
        # pop the top element from the stack and check if it is the corresponding open bracket
        elif c in (')', ']', '}'):
            # If the stack is empty, then there is no corresponding open bracket
            # so the input string is not valid
            if not stack:
                return False
            # Check if the top element on the stack is the corresponding open bracket
            # If it is not, then the input string is not valid
            if c == ')' and stack[-1] != '(':
                return False
            if c == ']' and stack[-1] != '[':
                return False
            if c == '}' and stack[-1] != '{':
                return False
            # If the top element on the stack is the corresponding open bracket,
            # remove it from the stack
            stack.pop()
    # If the stack is empty at the end, then all open brackets have been closed
    # so the input string is valid. Otherwise, it is not valid.
    return not stack
