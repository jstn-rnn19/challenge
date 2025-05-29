class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating
        self.is_favorite = False

    def mark_favorite(self):
        self.is_favorite = True

    def update_rating(self, new_rating):
        self.rating = new_rating

    def info(self):
        print(f"Title: {self.title}")
        print( f"Genre: {self.genre}" )
        print( f"Rating: {self.rating}" )
        print( f"Favorite: {self.is_favorite}" )


m1 = Movie("Inception", "Sci-Fi", 8.8)
m2 = Movie("The Godfather", "Crime", 9.2)
m1.update_rating(9.2)
m2.mark_favorite()
m1.info()
m2.info()
