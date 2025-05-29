class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.ISBN = isbn
        self.is_borrowed = False


    def get_borrow(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False

    def info(self):
        print(self.title)
        print( self.author )
        print( self.ISBN )
        print( self.is_borrowed )



b1 = Book("The Alchemist", "Paulo Coelho", 9780061122415)
b2 = Book("Atomic Habits", "James Clear", 9780735211292)

b1.get_borrow()


b1.info()
b2.info()