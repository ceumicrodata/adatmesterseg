# -*- coding: utf-8 -*-

# entering strings in the code itself
word = 'Apple'
print word

word = "Apple"
print word

multiline_text = '''Apple
Pear
Orange'''
print multiline_text

multiline_text = 'Apple\nPear\nOrange'
print multiline_text

# basic string methods
print word.lower()
print word.upper()
print 'this is a great book'.title()
print '   Apple '.strip()
print '   Apple!? '.strip('.?! ')

# slicing
print len('Apple')
print 'Apple'[0]
print 'Apple'[0:3]
print 'Apple'[-1]
print 'Apple'[-2:]
# strings behave as lists ('are iterable')
for letter in 'Apple':
	print letter

for line in multiline_text.splitlines():
	print len(line)


# character encoding
# store strings in memory as unicode
print type('Apple')
print type(u'Apple')
print u'Apple'
print unicode('Apple')
word = u'Apple'
for letter in word:
	print letter
print str(word)
print type(str(word))

# dont do this, you may get lucky, but is not guaranteed
word = 'árvíztűrő tükörfúrógép'
print type(word)
print word

uni_word = u'árvíztűrő tükörfúrógép'
print type(uni_word)
# dont do this, you may get lucky, but is not guaranteed
print uni_word

# encoding: mapping between unicode and byte strings
str_word = uni_word.encode('utf-8')
print type(str_word)
print str_word
print type(str_word.decode('utf-8'))

#str_word = uni_word.encode('latin1')
str_word = uni_word.encode('latin2')
str_word = uni_word.encode('windows-1250')
print type(str_word)
print str_word

# get rid of non acii letters
from unidecode import unidecode
literal = unidecode(uni_word)
print literal
# note: this is very different from 'decode', should rather be called 'transliterate'
literal = unidecode(u'Влади́мир Влади́мирович Пу́тин')
print literal
