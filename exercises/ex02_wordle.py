__author__: str = "730698517"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    i: int = 1
    while i <= 6:
        print(f"=== Turn {i}/6 ===")
        guess = input_guess(len(secret))
        result = emojified(guess, secret)
        print(result)
        if guess == secret:
            print(f"You won in {i}/6 turns!")
            return
        i = i + 1
    print(f"X/6 - Sorry, try again tomorrow!")


def contains_char(word: str, char: str) -> bool:
    "Function for finding char in word"
    assert len(char) == 1, f"len('{char}') is not 1"
    i: int = 0
    while i < len(word):
        if word[i] == char:
            return True
        else:
            i = i + 1
    return False


def emojified(guess: str, secret_word: str) -> str:
    "Checking if char is there"
    assert len(guess) == len(secret_word), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji: str = ""
    i: int = 0
    while i < len(secret_word):
        if guess[i] == secret_word[i]:
            emoji = emoji + GREEN_BOX
        elif contains_char(secret_word, guess[i]):
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
        i = i + 1
    return emoji


def input_guess(expected_length: int) -> str:
    """Looking for a guess"""
    guess = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


if __name__ == "__main__":
    main(secret="codes")
