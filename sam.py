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
        self.sentOrderedBooks = []

        self.id = Library.inst_num
        Library.inst_num += 1
    
    def decrementCounter(self):
        #if self.signedUp:
            #return True
        
        self.signUpCounter -= 1
            
        if self.signUpCounter <= 0:
            self.signUpCounter = 0
            self.signedUp = True

        

    def scan(self):

        booksToRemove = []
        booksToScan = []


            #print(self.books)

        for j, b in enumerate(self.books):
            if b == None:
                continue
            if b in scannedBooks:
                booksToRemove.append(j)
                #self.books.pop(j)
                continue
            #print(b)
            if len(booksToScan) < self.booksPerDay:
                booksToScan.append(b)
                self.sentOrderedBooks.append(b.id)
                #self.books.pop(j)
                booksToRemove.append(j)
                continue
            else:
                break
                #break
                
            
            #print(self.books)
            
        #for b in booksToScan:
            #self.books[b.id] = None
        
        #print(booksToScan)

        for i in booksToRemove:
            self.books[i] = None

        return booksToScan

    def getNumBooks(self):
        return len(list(b for b in self.books if b != None))

    def getScore(self):
        if self.getNumBooks() > 0:
            return (1/int(self.daysToSignUp)) * int(self.booksPerDay) * ((sum(list(b.score for b in self.books if b != None)) / self.getNumBooks()) / self.getNumBooks())
        return (1/int(self.daysToSignUp)) * int(self.booksPerDay) * 0

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

paths = [
    r"\\tawe_dfs\students\3\989623\Documents\GitHub\GoogleHash2020\a_example.txt",
    r"\\tawe_dfs\students\3\989623\Documents\GitHub\GoogleHash2020\b_read_on.txt",
    r"\\tawe_dfs\students\3\989623\Documents\GitHub\GoogleHash2020\c_incunabula.txt",
    r"\\tawe_dfs\students\3\989623\Documents\GitHub\GoogleHash2020\d_tough_choices.txt",
    r"\\tawe_dfs\students\3\989623\Documents\GitHub\GoogleHash2020\e_so_many_books.txt",
    r"\\tawe_dfs\students\3\989623\Documents\GitHub\GoogleHash2020\f_libraries_of_the_world.txt"
]

for file_path in paths:

    if os.path.exists(file_path.replace(".txt", "_out.txt")):
        continue

    allBooks, libraries, numDays = parseData(file_path)

    numAllBooks = len(allBooks)
    numLibraries = len(libraries)

    #for b in allBooks:
        #print(b.id, b.score)

    for l in libraries:
        print("l{} has [b{}] daysToSignUp{} booksPerDay{}".format(l.id, ", b".join(str(b.id) + " score" + str(b.score) for b in l.books), l.daysToSignUp, l.booksPerDay))

    currentDay = 0

    def getScore(l):
        return l.getScore()

    libraries.sort(key=getScore, reverse=True)

    signUpReady = True
    #signUpCounter = None
    currentLibrary = None
    scannedBooks = []
    signUpOrder = []
    while currentDay < numDays:

        #libraries.sort(key=getScore, reverse=True)
        #print(currentDay, "/", numDays)

        for l in libraries:

            #print(l.id, l.getScore())
                
            if signUpReady == True:
                if l.signedUp == False:
                    signUpReady = False
                    #print("signing up l{} - {} days remain - signed up {} - score {}".format(l.id, l.signUpCounter, str(l.signedUp), str(l.getScore())))
                    currentLibrary = l
                    signUpOrder.append(currentLibrary)
                    continue
            
            if l.signedUp:
                books = l.scan()
                if books:
                    #print("l{} scans [b{}]".format(l.id, ", b".join(str(b.id) + " score" + str(b.score) for b in books)))
                    for b in books:
                        #print("l{} scans [b{} score{}]".format(l.id, b.id, b.score))
                        scannedBooks.append(b)
            
            #libraries.sort(key=getScore, reverse=True)
        
        if currentLibrary != None:
                #print("signing up l{} - {} days remain - signed up {} - score {}".format(currentLibrary.id, currentLibrary.signUpCounter, str(currentLibrary.signedUp), str(currentLibrary.getScore())))
                currentLibrary.decrementCounter()
                if currentLibrary.signUpCounter <= 0:
                    signUpReady = True
                #currentLibrary.decrementCounter()

        currentDay += 1

    with open(file_path.replace(".txt", "_out.txt"), "w") as f:
        f.write(str(len(list(l for l in libraries if len(l.sentOrderedBooks) != 0))) + "\n")
        for l in libraries:
            if len(l.sentOrderedBooks) != 0:
                f.write(str(l.id) + " " + str(len(l.sentOrderedBooks)) + "\n")
                f.write(" ".join(str(bId) for bId in l.sentOrderedBooks) + "\n")
        f.close()
