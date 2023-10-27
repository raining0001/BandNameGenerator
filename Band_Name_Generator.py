import random
# import module 'random' in order to use it in the program 

print('Welcome to the Band Name Generator.')
#  prints the string

words = input('Input your favorite words : ').split()
# creates a variable 'words' that receives input from the user and creates a list using method '.spplit()'

print(words)
# print list 'words' in order to see

words_number = 2
# create constant literal 'words_number' and add value '2'

words_list = random.sample(words,words_number)
# create a variable that will get the value of the list 
# using the module random and variable '.sample'we will generate two random items from the list

first_words = words_list[0]
second_words = words_list[1]
# create two variables that contain the two items from the list with the index 0 and 1

print(f'Your band name is {(first_words).upper} {(second_words.upper)}')
# print string and the variable capitalized using method '().upper' in order to create the band name 

