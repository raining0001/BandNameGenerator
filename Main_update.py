from random import choice
from body import Main
from data import names, adj

Fav = []

print("Welcome to the band name generator")
questions = Main()
questions.generate()
questions.user_input()
questions.final()