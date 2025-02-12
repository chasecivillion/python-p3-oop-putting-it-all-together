#!/usr/bin/env python3

class Book:
    
    def __init__(self, title = "And Then There Were None", author = "Agatha Christie", page_count = 0):
        self.title = title
        self.author = author
        self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, page):
        if type(page) == int:
            self._page_count = page
        else:
            print("page_count must be an integer")

    page_count = property(get_page_count, set_page_count)





# def test_initialize_with_title(self):
#         '''gets initialized with a title.'''
#         Book("And Then There Were None")

#     def test_has_title(self):
#         '''has the title passed into __init__.'''
#         book = Book("And Then There Were None")
#         assert(book.title == "And Then There Were None")

#     def test_has_author_name(self):
#         '''can be assigned an author name.'''
#         book = Book("And Then There Were None")
#         book.author = "Agatha Christie"
#         assert(book.author == "Agatha Christie")

#     def test_has_page_count(self):
#         '''can be assigned a page count property.'''
#         book = Book("And Then There Were None")
#         book.page_count = 272
#         assert book.page_count == 272

#     def test_requires_int_page_count(self):
#         '''prints "page_count must be an integer" if page_count is not an integer.'''
#         book = Book("And Then There Were None")
#         captured_out = io.StringIO()
#         sys.stdout = captured_out
#         book.page_count = "not an integer"
#         sys.stdout = sys.__stdout__
#         assert captured_out.getvalue() == "page_count must be an integer\n"
#         assert not book.page_count

#     def test_has_genre(self):
#         '''can be assigned a genre.'''
#         book = Book("And Then There Were None")
#         book.genre = "Mystery"
#         assert(book.genre == "Mystery")

#     def test_can_turn_page(self):
#         '''outputs "Flipping the page...wow, you read fast!" when method turn_page() is called'''
#         book = Book("The World According to Garp")
#         captured_out = io.StringIO()
#         sys.stdout = captured_out
#         book.turn_page()
#         sys.stdout = sys.__stdout__
#         assert(captured_out.getvalue() == "Flipping the page...wow, you read fast!\n")
