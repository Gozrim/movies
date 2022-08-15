import pickle

from models import Movie


def save(obj_to_save, filename):
  with open(filename, "wb") as myfile:
    pickle.dump(obj_to_save, myfile)


def load(filename):
  with open(filename, "rb") as myfile:
    return pickle.load(myfile)

def read_movie_file():
  all_movies = []
  with open("movies.csv") as movie_file:
    movie_file.readline()
    for line in movie_file:
      temp_list = line.split(",")
      movie = Movie(film=temp_list[0],
                    genre=temp_list[1],
                    lead_studio=temp_list[2],
                    rotten_tomatoes=temp_list[3],
                    year=int(temp_list[4][:-1]))
      all_movies.append(movie)
  return all_movies

def first_time_read_data():
  all_movies = read_movie_file()
  save(all_movies, "movies.data")


if __name__ == "__main__":
    if input("are you sure?") == "yes":
        first_time_read_data()
