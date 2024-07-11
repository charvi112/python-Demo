class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

movie1 = Movie("M.S.Dhoni", "Neeraj Panday", 8.5)
movie2 = Movie("Black", "Sanjay leela Bhansali", 7)

print(f"Movie 1 - Title: {movie1.title}, Director: {movie1.director}, Rating: {movie1.rating}")
print(f"Movie 2 - Title: {movie2.title}, Director: {movie2.director}, Rating: {movie2.rating}")
