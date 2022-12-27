def decodeString(s: str) -> str:
    # create an empty stack to keep track of the current repetition count and character group
    stack = []
    for c in s:
        if c == "]":
            # pop the character group from the stack
            group = ""
            # keep popping characters from the stack until we reach the "[" character
            while stack[-1] != "[":
                group = stack.pop() + group
            # pop the "[" character from the stack
            stack.pop()
            # pop the repetition count from the stack
            count = ""
            # keep popping characters from the stack until we reach a character that is not a digit
            while stack and stack[-1].isdigit():
                count = stack.pop() + count
            # convert the repetition count to an integer
            count = int(count)
            # add the repeated character group to the stack
            stack.append(group * count)
        else:
            # if the character is not "]", just add it to the stack
            stack.append(c)
    # concatenate all the characters in the stack and return the result
    return "".join(stack)
