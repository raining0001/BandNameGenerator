from random import choice
from data import names, adj

class Main:
    def __init__(self, first = "", second= "", fav = ""):
        self.first = first
        self.second = second
        self.fav = fav

    def generate(self):
        self.first = choice(names)
        self.second = choice(adj)
    def user_input(self):
        self.fav = input("Please input your favorite word: ")

    def final(self):
        final_word = print(f"Your band name generator is {self.first} {self.second} {self.fav}.")
