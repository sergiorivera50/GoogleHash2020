import os
import math
import time
import random

class Book:
    def __init__(self, score):
        self.score = score

class Library:
    def __init__(self, books, daysToSignUp, booksPerDay):
        self.books = books
        self.daysToSignUp = daysToSignUp
        self.booksPerDay = booksPerDay

numBooks = None
numLibraries = None
numDays = 5

currentDay = 0

while currentDay < numDays:
    pass