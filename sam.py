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

        def getBookScore(b):
            return b.score
        
        self.books.sort(key=getBookScore, reverse=True)

        self.signedUp = False
        #self.numScanning = False
        self.signUpCounter = self.daysToSignUp
        #self.scanCounter = 1
        #self.signUpStartDay = None
        #self.signUpEndDay = None

        self.id = Library.inst_num
        Library.inst_num += 1
    
    def signUp(self):
        if self.signedUp:
            return True
            
        if self.signUpCounter <= 0:
            self.signedUp = True
            return True

        self.signUpCounter -= 1
        return False

    def scan(self):

        booksToRemove = []
        booksToScan = []

        for i in range(self.booksPerDay):

            for b in self.books:
                if b in scannedBooks:
                    booksToRemove.append(b)
                    continue
                booksToScan.append(b)
                break
            
        for b in booksToScan:
            self.books[b.id] = None

        for b in booksToRemove:
            self.books.pop(self.books.index(b))

        return booksToScan


    def getScore(self):
        return (1/int(self.daysToSignUp)) * int(self.booksPerDay) * ((sum(list(b.score for b in self.books)) / len(self.books)) / len(self.books))

def parseData(fileName):
    with open(fileName, "r") as f:
        lines = list(l.strip() for l in f.readlines())
        f.close()

    initData = lines[0].split()
    numBooks = int(initData[0])
    numLibraries = int(initData[1])
    days = int(initData[2])

    #print(numBooks, numLibraries, days)
    
    bookScores = lines[1].split()
    #print(bookScores)

    allBooks = []
    for i in range(numBooks):
        allBooks.append(Book(int(bookScores[i])))

    libraries = []
    libraryCount = 0
    count = 2
    for i in range(numLibraries):
        libraryData = lines[count].split()
        numBooks = int(libraryData[0])
        libraryBooksIds = lines[count+1].split() # get book ids for this library from next line
        libraryBooks = []
        for i in libraryBooksIds:
            libraryBooks.append(allBooks[int(i)])
        libraries.append(Library(libraryBooks, int(libraryData[1]), int(libraryData[2])))
        count += 2 # jump to the next library
        libraryCount += 1

    return allBooks, libraries, days

def getBookById(id):
    return allBooks[id]

# GET INPUT DATA

allBooks, libraries, numDays = parseData("a_example.txt")

numAllBooks = len(allBooks)
numLibraries = len(libraries)

for b in allBooks:
    print(b.id, b.score)

for l in libraries:
    print("l{} has [b{}] daysToSignUp{} booksPerDay{}".format(l.id, ", b".join(str(b.id) + " score" + str(b.score) for b in l.books), l.daysToSignUp, l.booksPerDay))

currentDay = 0

def getScore(l):
    return l.getScore()

libraries.sort(key=getScore, reverse=True)

currentLibrary = None
scannedBooks = []
while currentDay < numDays:
    for l in libraries:
        #print(l.id, l.getScore())
            
        if not l.signUp():
            print("signing up l{} - {} days remain - signed up {} - score {}".format(l.id, l.signUpCounter, str(l.signedUp), str(l.getScore())))
            currentLibrary = l.id
            break

        books = l.scan()
        if books:
            print("l{} scans [b{}]".format(l.id, ", b".join(str(b.id) + " score" + str(b.score) for b in books)))
            scannedBooks.append(book)
        
    
    #input()
    currentDay += 1