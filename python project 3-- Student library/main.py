class Library:
    def __init__(self,listOfBooks):
        self.books=listOfBooks

    def displayAvailableBooks(self):
        print("Books present in the library are: ")
        for book in self.books:
            print(" *" + book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued the book {bookName},Please keep it safe and return it within 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print(f"{bookName} have already been issued to someone else,Please wait until it is returned!")
            return False
    
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning this book. Hope you enjoyed reading it. Have a great day ahead!")
    
class Student:
    def requestBook(self):
        self.book = input("Enter the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the book you want to return: ")
        return self.book

if __name__=="__main__":
    centralLibrary= Library(["Algorithms","Database","Python notes","Intro to c++","BTS"])
    student=Student()
    # centralLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''***Welcome to Central Library***
        Please choose an option:
        1. Listing all books
        2. Request a book
        3. Add/Return book
        4. Exiting the library 
        '''
        print(welcomeMsg)
        a=int(input("Enter your choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for using this library!")
            exit()
        else:
            print("Invalid choice")