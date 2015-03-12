# -*- coding: utf-8 -*-
from typoglicemia import typoglicemia
from unittest import TestCase, main

DOUBLE = ('cs', 'dz', 'gy', 'ly', 'ny', 'sz', 'ty', 'zs')
TRIPLE = ('dzs',)
ACCENTED = (u'á', u'ó', u'ú', u'é', u'í', u'ö', u'ő', u'ü', u'ű')

def first_and_last_letter_english(word):
    return "".join([word[0], word[-1]])

def words(line):
    return line.split()

class ParsingTests(TestCase):
    def test_single_space(self):
        pass

    def test_multiple_spaces(self):
        pass

    def test_other_whitespace(self):
        pass

class NottheSame(TestCase):
    def test_long_word_not_the_same(self):
        be = 'abcdefghijklmnopqrst'
        self.assertNotEqual(typoglicemia(be), be)

class EnglishTests(TestCase):
    def test_one_word(self):
        self.assertEqual(first_and_last_letter_english(typoglicemia('abcdef')), 'af')

    def test_length_of_word(self):
        self.assertEqual(len(typoglicemia('abcdef')), len('abcdef'))

    def test_multiple_words(self):
        be = 'abcdef ghijkl'
        be_chars = [first_and_last_letter_english(word) for word in words(be)]
        ki_chars = [first_and_last_letter_english(word) for word in words(typoglicemia(be))]
        self.assertListEqual(ki_chars, be_chars)

    def test_same_characters(self):
        self.assertSetEqual(set(typoglicemia('abcdef')), set('abcdef'))

class HungarianTests(TestCase):
    def test_double_letters_at_beginning(self):
        for letter in DOUBLE:
            be = letter+'bcdef'
            self.assertEqual(typoglicemia(be)[0:2], letter)
            self.assertEqual(typoglicemia(be)[-1], 'f')

    def test_double_letters_at_end(self):
        for letter in DOUBLE:
            be = 'abcde'+letter
            self.assertEqual(typoglicemia(be)[-2:], letter)
            self.assertEqual(typoglicemia(be)[0], 'a')

    def test_double_letters_in_middle(self):
        pass

    def test_accents_at_beginning(self):
        for letter in ACCENTED:
            be = letter+'bcdef'
            self.assertEqual(typoglicemia(be)[0], letter)
            self.assertEqual(typoglicemia(be)[-1], 'f')

    def test_accents_at_end(self):
        for letter in ACCENTED:
            be = 'abcde'+letter
            self.assertEqual(typoglicemia(be)[-1], letter)
            self.assertEqual(typoglicemia(be)[0], 'a')

    def test_accents_in_middle(self):
        pass

    def test_triple_letters_at_beginning(self):
        for letter in TRIPLE:
            be = letter+'bcdef'
            self.assertEqual(typoglicemia(be)[0:3], letter)
            self.assertEqual(typoglicemia(be)[-1], 'f')

    def test_triple_letters_at_end(self):
        for letter in TRIPLE:
            be = 'abcde'+letter
            self.assertEqual(typoglicemia(be)[-3:], letter)
            self.assertEqual(typoglicemia(be)[0], 'a')

    def test_triple_letters_in_middle(self):
        pass


if __name__ == '__main__':
    main()
