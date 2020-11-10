import re

from printer import Printer
from word_provider import WordProvider

MAX_ERRORS = 7


class Game:
    def __init__(self, words, printer):
        self.words = words
        self.printer = printer

        self.word = self.pick_random_word()
        self.errors = 0
        self.letters = ''

    def run(self):
        self.show_game_title()
        self.show_hint(self.hint())
        while self.still_alive() and not self.all_letters_guessed():
            self.run_turn()

        self.show_final_result()

    def still_alive(self):
        return self.errors < MAX_ERRORS

    def run_turn(self):
        letter = self.ask_player_for_letter()
        if letter in self.word:
            self.append_letter(letter)
        else:
            self.increment_error_count()
        self.partial_score()

    def append_letter(self, letter):
        self.letters += letter

    def increment_error_count(self):
        self.errors += 1

    def partial_score(self):
        self.show_hint(self.hint())
        self.show_hangman()

    def end_message(self):
        return self.success_message() if self.all_letters_guessed() else self.fail_message()

    def fail_message(self):
        self.printer.writeln('Buuuu')

    def success_message(self):
        self.printer.success(self.errors)

    def ask_player_for_letter(self):
        return input('Introduce una letra: ')

    def pick_random_word(self):
        return self.words.random()

    def all_letters_guessed(self):
        if self.letters == '':
            return
        remaining = re.sub(f'[{self.letters}]', '', self.word)
        return len(remaining) == 0

    def hint(self):
        if self.letters == '':
            return '_' * len(self.word)
        return re.sub(f'[^{self.letters}]', '_', self.word)

    def show_game_title(self):
        self.printer.title('Adivina la palabra')

    def show_hint(self, hint):
        self.printer.hint(hint)

    def show_hangman(self):
        self.printer.hangman(self.errors)

    def show_final_result(self):
        self.end_message()
        self.printer.word(self.word)


if __name__ == '__main__':
    game = Game(WordProvider(), Printer())
    game.run()
