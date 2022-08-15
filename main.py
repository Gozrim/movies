
# step 1: read the movies from file
# step 2: build a list of Movie objects
from models import Movie
from util import save, load


# starting program - reading from file

# delete one movie
# main_movies_class.my_list = main_movies_class.my_list[:-1]
# save(main_    movies_class, "movies.data")


all_movies = load("movies.data")
print(all_movies[0].film)
# all_movies[0].file="Minions 2"
# save(all_movies,"movies.data")

import random

print(random.choices([1,2,3,4,5,6,7,8,9,10],k=6))





