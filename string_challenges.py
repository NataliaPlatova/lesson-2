# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв а в слове
word = 'Архангельск'
print(word.lower().count('а'))  # Добавила lower


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ['а', 'я', 'о', 'ё', 'у', 'ю', 'ы', 'и', 'э', 'е']
number_of_vowels = 0
word = word.lower()
for character in word:  # Индекс убрала
    if character in vowels:
        number_of_vowels += 1
print(number_of_vowels)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
spl_sentence = sentence.split()
for word in spl_sentence:   # Индекс убрала
    print(word[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
sum = 0
spl_sentence = sentence.split()
for word in spl_sentence:   # Индекс убрала
    sum = sum + len(word)
print(sum/(len(spl_sentence)))