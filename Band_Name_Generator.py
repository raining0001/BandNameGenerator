import random

print('Welcome to the Band Name Generator.')
words = input('Input your favorit words : ').split()
print(words)
words_number = 2

words_list = random.sample(words,words_number)

first_words = words_list[0]
second_words = words_list[1]

print(f'Your band name is {first_words} {second_words}')



