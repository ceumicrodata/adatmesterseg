from typoglicemia import typoglicemia
from unittest import TestCase, main

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
        pass

    def test_double_letters_at_end(self):
        pass

    def test_double_letters_in_middle(self):
        pass

    def test_accents_at_beginning(self):
        pass

    def test_accents_at_end(self):
        pass

    def test_accents_in_middle(self):
        pass

    def test_dzs_is_not_zs(self):
        pass

if __name__ == '__main__':
    main()
