# Library Book System(Class and Class Attribute)

# Create a class Libarary Book that:
# Has a class attribute total_books (shared by all books)

# An init method to initialize title,author, and year

# A display_book() method to show book details

# A method add_book() that increments total_books


# Create three book objects and update total books

class LibraryBook:
    total_books = 0
    def __init__(self,title, author,year):
        self.title = title
        self.author = author
        self.year = year
        LibraryBook.total_books += 1
    
    def display_book(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
    
    
        
        
book1 = LibraryBook("Open Heavens", "E.A Adeboye" , 2024)

book2 = LibraryBook("Lion and the Jewel", "Wole Soyinka", 1990 )

book3 = LibraryBook("Lorem Ipsum", "Ayoola Ojo",2026)


book1.display_book()
book2.display_book()
book3.display_book()


print(f"Total books in the Library :{LibraryBook.total_books} ")
    
    

    
