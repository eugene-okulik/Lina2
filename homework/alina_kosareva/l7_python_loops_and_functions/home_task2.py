words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def new_word(key, value):
    print(key * value)


for key, value in words.items():
    new_word(key, value)
