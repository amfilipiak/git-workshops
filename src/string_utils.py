import random
from string import ascii_lowercase


def random_alpha():
    return random.choice(ascii_lowercase)


def random_delete(word_as_array):
    place = random.randint(0, len(word_as_array) - 1)
    del word_as_array[place]
    return word_as_array


def random_add(word_as_array):
    place = random.randint(0, len(word_as_array))
    word_as_array.insert(place, random_alpha())
    return word_as_array


def random_replace(word_as_array):
    if not len(word_as_array):
        return word_as_array
    place = random.randint(0, len(word_as_array) - 1) if len(word_as_array) > 1 else 0
    word_as_array[place] = random_alpha()
    return word_as_array


_noise_fun = [random_delete, random_add, random_replace]

# assume all are lowercase
def add_noise(word, n_changes=1):
    noisy = [c for c in word]
    for i in range(n_changes):
        start = 0 if len(noisy) > 1 else 1
        noisy = random.choice(_noise_fun[start:])(noisy)
    return "".join(noisy)


def random_word():
    with open("res/words.txt",mode="rt") as f:
        line = next(f)
        for num, aline in enumerate(f, 2):
            if not random.randrange(num):
                line = aline
            print(line)
        return line.strip()
