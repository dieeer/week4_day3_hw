class Book:
    
    def __init__(self, title, year_released, genre, id = None):
        self.title = title
        self.year_released = year_released
        self.genre = genre
        self.id = id