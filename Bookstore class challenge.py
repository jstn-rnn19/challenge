class Bookstore:
    def __init__(self, storename):
        self.storename = storename
        self.inventory = []
        self.sales_count = 0

    def add_book(self, book_title):
        self.inventory.append(book_title)

    def sell_book(self, book_title):
        if book_title in self.inventory:
            self.inventory.remove( book_title )
            self.sales_count += 1
        else:
            print("no item")


    def show_inventory(self):
        for item in self.inventory:
            print(f"{item}")

    def report_sales(self):
        print(f"Sale: {self.sales_count}")

    def info(self):
        print(f"Name of Store: {self.storename}")
        print( f"Inventory: {self.inventory}" )
        print( f"Sales: {self.sales_count}" )

b1 = Bookstore("justine")
b1.add_book("Atomic Habits")
b1.add_book("negotiation")
b1.sell_book("HAHAHAHA")

b1.info()