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

def parseData(fileName):
    with open(fileName, "r") as f:
        lines = list(l.strip() for l in f.readlines())
        f.close()

    initData = lines[0].split()
    numBooks = int(initData[0])
    numLibraries = int(initData[1])
    days = int(initData[2])

    print(numBooks, numLibraries, days)
    
    bookScores = lines[1].split()
    print(bookScores)

    allBooks = []
    for i in range(numBooks):
        allBooks.append(Book(bookScores[i]))

    libraries = []
    libraryCount = 0
    count = 2
    for i in range(numLibraries):
        libraryData = lines[count].split()
        numBooks = int(libraryData[0])
        libraryBooksIds = lines[count+1].split() # get book ids for this library from next line
        libraryBooks = []
        #for j in range(len(libraryBooksIds)):
            #for book in allBooks:
                #if book.id == int(libraryBooksIds[j]):
                    #libraryBooks.append(book)
        for i in libraryBooksIds:
            libraryBooks.append(allBooks[int(i)])
        libraries.append(Library(libraryBooks, libraryData[1], libraryData[2]))
        count += 2 # jump to the next library
        libraryCount += 1

    return allBooks, libraries, days

def getBookById(id):
    return allBooks[id]

allBooks, libraries, numDays = parseData("a_example.txt")

numAllBooks = len(allBooks)
numLibraries = len(libraries)

#allBooks = []
#libraries = []

#for i in range(numAllBooks):
    #score = random.randint(0, 10**3)
    #allBooks.append(Book(score))

#for i in range(numLibraries):
    #numberOfBooks = random.randint(1, numAllBooks)
    #daysToSignUp = random.randint(1, 10**5)
    #booksPerDay = random.randint(1, 10**5)
    
    #books = []
    #pool = list(range(numAllBooks))
    #for b in range(numberOfBooks):
        # get ids
        #choice = random.choice(pool)
        #pool.pop(pool.index(choice))
        #books.append(getBookById(choice))

    #libraries.append(Library(books, daysToSignUp, booksPerDay))

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