from datetime import date

class Author:
    def __init__(self,name):
        self.name = name
        self.book = None

    def addBook(self, myBook):
        self.book = myBook

class Book:
    def __init__(self, name, pubDate):
        self.name = name
        self.pubDate = pubDate

author1 = Author("Miika")
book1 = Book("Dragons & Kings", date.today())
author1.addBook(book1)

print(author1.book.name)
print(author1.book.pubDate)
