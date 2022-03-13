import json

exclude_letters = [
    'g',
    # 'i',
    'k',
    'm',
    # 'o',
    'q',
    'v',
    'w',
    'x',
    'z',
]


def load_words(source='./words_dictionary.json', as_list=True):
    with open(source, 'r') as word_file:
        valid_words = json.loads(word_file.read())

    word_file.close()
    return list(valid_words.keys()) if as_list else valid_words.keys()


if __name__ == '__main__':
    words = load_words()

    filtered = [word for word in words if not any([letter for letter in exclude_letters if letter in word])]
    filtered.sort(key=len)
    longest = filtered[-1]
    print("\nLongest word for 7-segment display: {} ({} letters)".format(longest, len(longest)))
