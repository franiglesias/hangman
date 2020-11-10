class Printer:
    def success(self, error_count):
        self.write(f'Enhorabuena. {self.__texts(error_count)}')

    @staticmethod
    def __texts(index):
        texts = {
            0: 'Perfecto.',
            1: 'Acertaste.',
            2: 'Muy bien.',
            3: 'Buena.',
            4: 'Esta era difícil.',
            5: 'Ha costado, ¿eh?',
            6: 'Ha ido de un pelo.'
        }
        return texts[index]

    def hangman(self, error_count):
        if error_count == 0:
            return

        parts = self.__parts_of_hangman(error_count)

        self.write('+---+')
        for line in parts:
            self.write('|  ' + line)
        self.write('|')
        self.write('+---------')

    @staticmethod
    def __parts_of_hangman(index):
        parts = {
            7: [' | ', ' O ', '/|\\', '/ \\'],
            6: [' O ', '/|\\', '/ \\'],
            5: [' O ', '/|\\', '/  '],
            4: [' O ', '/|\\'],
            3: [' O ', '/| '],
            2: [' O ', '/ '],
            1: [' O '],
        }
        return parts[index]

    def hint(self, hint):
        self.writeln(hint.replace("", " ")[1: -1])

    def word(self, word):
        self.writeln(f'La palabra era... {word}')

    def writeln(self, line):
        self.write(line + '\n')

    @staticmethod
    def write(line):
        print(line)

    def title(self, line):
        bar = '=' * len(line)
        self.write(line)
        self.writeln(bar)

