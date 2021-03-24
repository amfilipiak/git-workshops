import random
from string import ascii_lowercase,punctuation,digits


class StringUtils(object):

    _chars = ascii_lowercase+punctuation+digits

    def random_word(self, max_length):
        return "".join(random.choices(ascii_lowercase, k=random.randint(1, max(1,max_length))))

    def random_sentence(self, max_word_length, length=5):
        return " ".join(self.random_word(max_word_length) for _ in range(length))

    def random_word_replace(self, sentence, max_word_length):
        parts = sentence.split()
        to_replace = random.randint(0,len(parts)-1)
        parts[to_replace] = self.random_word(max_word_length)
        return " ".join(parts)

    @staticmethod
    def random_char():
        return random.choice(StringUtils._chars)


    @staticmethod
    def random_alpha():
        return random.choice(ascii_lowercase)


    @staticmethod
    def random_delete(word_as_array):
        place = random.randint(0, len(word_as_array) - 1)
        del word_as_array[place]
        return word_as_array


    @staticmethod
    def random_add(word_as_array):
        place = random.randint(0, len(word_as_array))
        word_as_array.insert(place, StringUtils.random_alpha())
        return word_as_array


    @staticmethod
    def random_replace(word_as_array):
        if not len(word_as_array):
            return word_as_array
        place = random.randint(0, len(word_as_array) - 1) if len(word_as_array) > 1 else 0
        word_as_array[place] = StringUtils.random_alpha()
        return word_as_array


    # assume all are lowercase
    @staticmethod
    def add_noise(word, n_changes=1):
        noisy = [c for c in word]
        for i in range(n_changes):
            start = 0 if len(noisy) > 1 else 1
            noisy = random.choice(_noise_fun[start:])(noisy)
        return "".join(noisy)


_noise_fun = [StringUtils.random_delete, StringUtils.random_add, StringUtils.random_replace]
