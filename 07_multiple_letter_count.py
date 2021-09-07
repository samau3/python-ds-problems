def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_list = {}
    for letter in phrase:
        if not (letter in letter_list.keys()):
            letter_list[letter] = 1
        else:
            letter_list[letter] += 1
    return letter_list

    # letter_list = {letter for letter in phrase }