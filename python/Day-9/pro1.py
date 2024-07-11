class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")


book1 = Book("Bunch of old Letters", "jawaharlal Nehru", 1960)
book2 = Book("1984", "George Orwell", 1949)

book1.display_info()
print()  
book2.display_info()
