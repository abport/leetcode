def getHint(secret: str, guess: str) -> str:
    # Initialize hashmaps to store the counts of the digits in secret and guess
    secret_counts = {}
    guess_counts = {}

    # Initialize the counts of bulls and cows
    bulls = 0
    cows = 0

    # Iterate through the digits in the guess string
    for i in range(len(guess)):
        # Check if the digit is a bull
        if secret[i] == guess[i]:
            bulls += 1
        else:
            # If the digit is not a bull, increment the count of the digit in the guess hashmap
            if guess[i] in guess_counts:
                guess_counts[guess[i]] += 1
            else:
                guess_counts[guess[i]] = 1
            # Increment the count of the digit in the secret hashmap
            if secret[i] in secret_counts:
                secret_counts[secret[i]] += 1
            else:
                secret_counts[secret[i]] = 1

    # Iterate through the keys in the guess hashmap
    for key in guess_counts.keys():
        # If the key is also present in the secret hashmap, increment the count of cows by the minimum of the two counts
        if key in secret_counts:
            cows += min(guess_counts[key], secret_counts[key])

    # Return the hint in the required format
    return f"{bulls}A{cows}B"
