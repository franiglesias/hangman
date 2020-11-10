import random


class WordProvider:
    def __init__(self):
        self.words_file = 'palabras.txt'

    def random(self):
        return self.read_random()

    def read_random(self):
        file_object = open(self.words_file)
        number_of_lines = 0
        selected = ''

        while 1:
            line = file_object.readline()
            if not line:
                break
            number_of_lines += 1

            if random.uniform(0, number_of_lines) < 1:
                selected = line

        file_object.close()
        return selected.strip().lower()
