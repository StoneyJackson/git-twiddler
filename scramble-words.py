import random
import re
import sys
import argparse


def main():
    args = get_commandline_arguments()
    probability_word_is_twiddled = float(args.p)
    max_word_length = args.max_word_length
    min_word_length = args.min_word_length

    token_filter = TokenFilter(min_word_length, max_word_length)

    lines = read_lines()
    tokens = tokenize_lines(lines)
    tokens = twiddle_random_words(probability_word_is_twiddled, tokens, token_filter)
    for t in tokens:
        if t.is_twiddled():
            string = t.get_twiddled()
        else:
            string = t.get_string()
        print(string, end='')


def get_commandline_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('p', help='Probability that a word is twiddled.', type=float)
    parser.add_argument('--max-word-length', help='The maximum length of a word to be twiddled.',
            type=int, default=float('inf'))
    parser.add_argument('--min-word-length', help='The minimum length of a word to be twiddled.',
            type=int, default=2)
    args = parser.parse_args()
    return args


def read_lines():
    for line in sys.stdin:
        yield line


def tokenize_lines(lines):
    for line_number, line in enumerate(lines, start=1):
        character_number = 1
        for string in re.split(r'(\s+)', line):
            yield Token(line_number, character_number, string)
            character_number += len(string)


def twiddle_random_words(probability_word_is_twiddled, tokens, token_filter):
    for token in tokens:
        if token_filter.is_twiddleable(token):
            if random.random() < probability_word_is_twiddled:
                token.try_to_twiddle()
        yield token


class TokenFilter:
    def __init__(self, min_word_length, max_word_length):
        self._min_word_length = min_word_length
        self._max_word_length = max_word_length

    def is_twiddleable(self, token):
        string = token.get_string()
        if string is None:
            return False
        if not self._min_word_length <= len(string) <= self._max_word_length:
            return False
        if self._all_same_character(string):
            return False
        if self._contains_non_alphabetic_characters(string):
            return False
        return True

    def _all_same_character(self, string):
        return re.fullmatch(r'(.)\1*', string) is not None

    def _contains_non_alphabetic_characters(self, string):
        return re.fullmatch('[a-zA-Z]+', string) is None


class Token:
    def __init__(self, line_number, character_number, string):
        self._line_number = line_number
        self._character_number = character_number
        self._string = string
        self._twiddled = None

    def try_to_twiddle(self):
        for i in range(100):
            string_list = list(self._string)
            random.shuffle(string_list)
            self._twiddled = ''.join(string_list)
            if self._twiddled != self._string:
                break
        if self._twiddled == self._string:
            self._twiddled = None

    def is_twiddled(self):
        return self._twiddled is not None

    def get_string(self):
        return self._string

    def get_twiddled(self):
        return self._twiddled


if __name__ == '__main__':
    main()
