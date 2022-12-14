#Поле чудес

from random import randint

lst = ['анабиоз', 'доверие', 'маринад', 'полусвет',
       'стол', 'водонагреватель', 'плеоназм']
word_cpu = lst[randint(0, len(lst) - 1)]
print(f'Компьбютер загадал слово из {len(lst)} букв')

def guessing_letters(word):
    count = 0
    str_replase = word
    while count < len(word):
        letter = str(input("Введите букву: "))
        if len(letter) > 1:
            print('Вы ввели более одного символа')
            continue
        if letter in str_replase:
            count += 1
            print(f'Буква "{letter}" есть в этом слове, осталось отгадать {len(word) - count}')
            str_replase = str_replase.replace(letter, '', 1)
        else:
            print('Попробуйте еще раз')
            continue
print(word_cpu)
guessing_letters(word_cpu)
print(f'Вы отгадали! Это слово - {word_cpu}')