from docx import Document
from yargy import rule 
from yargy.predicates import eq as eq_
from yargy.tokenizer import Tokenizer


symbols_to_mirror = ['(', ')', '/']


def get_docx_text(path):
    document = Document(path)
    paragraphs = []
    for paragraph in document.paragraphs:
        paragraphs.append(paragraph.text)
    text = "\n".join(paragraphs)
    while(text.find("  ") > -1):
        text = text.replace("  ", " ")
    while(text.find("\t\t") > -1):
        text = text.replace("\t\t", "\t")
    while(text.find("\n\n") > -1):
        text = text.replace("\n\n", "\n")
    return text


# Возвращает регулярку, описывающую текст между строками x1 и x2.
def regex_between(x1, x2, is_strict=False, str_end=""):
    if type(x1) is list:
        x1 = f"{str_end}|".join(x1)
    if type(x2) is list:
        x2 = f"|".join(x2)
    x1 += str_end
    for symbol in symbols_to_mirror:
        x1 = x1.replace(symbol, f'\{symbol}')
        x2 = x2.replace(symbol, f'\{symbol}')
    if is_strict:
        return f'(?<={x1}\n).+?(?={x2})'
    return f'(?<={x1}\n)(.|\n)*(?={x2})'


'''
Принимает на вход list строк вида 'слово-1 слово-2 ... слово-n'.
Возвращает tuple правил вида rule(eq_('слово-1'), eq_('слово-2'), ..., eq_('слово_n'))
'''
def list_to_eq_seq(list_of_str: list [str]):
    tokenizer = Tokenizer()
    rules = []
    for el in list_of_str:
        print(el, end="\n\n")
        eq_seq = rule(*(eq_(subel.value) for subel in tokenizer(el)))
        print(eq_seq, end='\n\n')
        rules.append(eq_seq)
    return tuple(rules)


def print_tree(tree, indent=0):
    print(f'{'\t'*indent*2}{tree}', end='\n\n')
    if tree.children is not None:
        for child in tree.children:
            print_tree(child, indent+1)


if __name__ == "__main__":
    pass