from random import shuffle

DOUBLE = ('cs', 'dz', 'gy', 'ly', 'ny', 'sz', 'ty', 'zs')
TRIPLE = ('dzs',)

def typoglicemia(text):
    return u' '.join([u''.join(typoglicemia_of_a_list(convert_text_to_list(word))) for word in split_to_words(text)])

def typoglicemia_of_a_list(iterable):
    if len(iterable)>=4:
        # shorter lists need not be reshuffled
        middle = iterable[1:-1]
        # 'shuffle' shuffles in place, does not return a value!
        shuffle(middle)
        return [iterable[0]]+middle+[iterable[-1]]
    else:
        return iterable

def convert_text_to_list(text):
    if text == '':
        return []
    if text[0:3] in TRIPLE:
        return [text[0:3]] + convert_text_to_list(text[3:])
    if text[0:2] in DOUBLE:
        return [text[0:2]] + convert_text_to_list(text[2:])
    else:
        return [text[0]] + convert_text_to_list(text[1:])

def split_to_words(text):
    return text.split()

def read_text():
    pass

def write_text():
    pass

if __name__ == '__main__':
    text = read_text()
    output = typoglicemia(text)
    write_text(output)
