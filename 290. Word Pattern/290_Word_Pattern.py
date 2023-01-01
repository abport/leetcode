def wordPattern(pattern: str, s: str) -> bool:
    # create a dictionary to store the mapping from characters
    # in the pattern to words in the string
    char_to_word = {}
    # create a set to store the words that have already been mapped
    # to a character in the pattern
    mapped_words = set()

    # split the string into a list of words
    words = s.split()

    # check if the number of characters in the pattern
    # is not equal to the number of words in the string
    if len(pattern) != len(words):
        return False

    # iterate through the characters in the pattern
    for i, char in enumerate(pattern):
        # get the word at the current index
        word = words[i]

        # check if the character has already been mapped to a word
        if char in char_to_word:
            # check if the word for the current character is not
            # the same as the current word
            if char_to_word[char] != word:
                return False
        else:
            # check if the current word has already been mapped
            # to a character in the pattern
            if word in mapped_words:
                return False
            # map the character to the word and add the word
            # to the set of mapped words
            char_to_word[char] = word
            mapped_words.add(word)

    # if no issues were found, return True
    return True
