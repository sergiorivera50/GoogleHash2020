import os
import math
import time
import random

class Book:
    inst_num = 0
    def __init__(self, score):
        self.score = score
        self.id = Book.inst_num
        Book.inst_num += 1

class Library:
    inst_num = 0
    def __init__(self, books, daysToSignUp, booksPerDay):
        self.books = books
        self.daysToSignUp = daysToSignUp
        self.booksPerDay = booksPerDay

        self.signedUp = False
        self.signUpStartDay = None
        self.signUpEndDay = None

        self.id = Book.inst_num
        Book.inst_num += 1
    
    def signUp(self):
        if self.signUpStartDay == None:
            self.signUpStartDay = currentDay
            self.signUpEndDay = self.signUpStartDay + self.daysToSignUp
        else:
            if currentDay >= self.signUpEndDay:
                return True
        return False

def getBookById(id):
    return allBooks[id]

numAllBooks = 6
numLibraries = 2
numDays = 7

allBooks = []
libraries = []

for i in range(numAllBooks):
    score = random.randint(0, 10**3)
    allBooks.append(Book(score))

for i in range(numLibraries):
    numberOfBooks = random.randint(1, numAllBooks)
    daysToSignUp = random.randint(1, 10**5)
    booksPerDay = random.randint(1, 10**5)
    
    books = []
    pool = list(range(numAllBooks))
    for b in range(numberOfBooks):
        # get ids
        choice = random.choice(pool)
        pool.pop(pool.index(choice))
        books.append(getBookById(choice))

    libraries.append(Library(books, daysToSignUp, booksPerDay))

for b in allBooks:
    print(b.id, b.score)

for l in libraries:
    print("l{} has [b{}]".format(l.id, ", b".join(str(b.id) + " score" + str(b.score) for b in l.books)))

currentDay = 0

#with open("b_read_on.txt", "r") as f:
    #print(f.read())

#print(os.listdir())

while currentDay < numDays:
    #print("hello")
    pass