class Publication:
    def __init__(self,title,author):
        self._title = title
        self._author = author

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def set_title(self, new_title):
        self._title = new_title

    def set_author(self, new_author):
        self._author = new_author

    def display_info(self):
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")

class Book(Publication):
    def __init__(self,title,author,number_pages):
        super().__init__(title,author)
        self._number_pages = number_pages

    def get_number_of_pages(self):
        print(f"Number of Pages: {self._number_pages}")

    def set_number_of_pages(self, new_number_pages):
        if new_number_pages < 1:
            print("Number of pages must be positive.")
        else:
            self._number_pages = new_number_pages

class Magazine(Publication):
    def __init__(self,title,author,issue_number):
        super().__init__(title,author)
        self._issue_number = issue_number

    def get_issue_number(self):
        print(f"Issue Number: {self._issue_number}")

    def set_issue_number(self, new_issue_number):
        self._issue_number = new_issue_number

pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

#Printing the information 
print ("Publication Information:")
pub1.display_info()

print ("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
book1.get_number_of_pages()

print ("\nMagazine Information:")
mag1.display_info()
mag1.get_issue_number()