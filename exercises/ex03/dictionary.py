__author__ = "730698517"


def invert(initial: dict[str, str]) -> dict[str, str]:
    """To invert the keys and values of a dict"""
    temp: dict[str, str] = {}
    for key in initial:
        value = initial[key]
        if value in temp:
            raise KeyError("Duplicate key")
        temp[value] = key
    return temp


def count(input: list[str]) -> dict[str, int]:
    """To count the number of times a value has appeared"""
    temp: dict[str, int] = {}
    i = 0
    while i < len(input):
        key = input[i]
        if key in temp:
            temp[key] += 1
        else:
            temp[key] = 1
        i += 1
    return temp


def favorite_color(choices: dict[str, str]) -> str:
    """Finds the most common favorite color"""
    color_counts: dict[str, int] = {}
    for key in choices:
        color = choices[key]
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1
    most_common_color = ""
    highest_count = 0
    for color in color_counts:
        if color_counts[color] > highest_count:
            most_common_color = color
            highest_count = color_counts[color]
    return most_common_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Bins a list of strings by their length into a dictionary"""
    bin: dict[int, set[str]] = {}
    for word in words:
        word_len = len(word)
        if word_len in bin:
            current_set = bin[word_len]
            if word not in current_set:
                bin[word_len] = set(list(current_set) + [word])
        else:
            bin[word_len] = {word}
    return bin
