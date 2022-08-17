class Book:
    
    def __init__(self, title, year_released, genre, author, id = None,):
        self.title = title
        self.year_released = year_released
        self.genre = genre
        self.author = author
        self.id = id