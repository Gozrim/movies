
class Movie:
    all_movies = []
    def __init__(self, film, genre, lead_studio,rotten_tomatoes,year):
        self.year = year
        self.rotten_tomatoes = rotten_tomatoes
        self.lead_studio = lead_studio
        self.genre = genre
        self.film = film

    def __str__(self):
        return f"{self.film}, {self.genre}, {self.lead_studio}, {self.year}"

    @staticmethod
    def search(genre):
        results = []
        for mov in Movie.all_movies:
            if mov.genre == genre:
                results.append(mov)
        return result





#
#
# class Hall:
#     def __init__(self, hall_type, price):
#         self.price = price
#         self.hall_type = hall_type
#
#
# class Screening:
#     def __init__(self, movie, hall, time):
#         self.time = time
#         self.hall = hall
#         self.movie = movie
#         self.number_of_tickets = 100
#
#     def buy_ticket(self, number_of_tickets):
#         screening.number_of_tickets = screening.number_of_tickets - number_of_tickets
#         print("the price is ", screening.hall.price * number_of_tickets)
#
# movie1 = Movie(film="minions",genre="Animation",lead_studio="Illumination",rotten_tomatoes=95,year=2022)
# hall1 = Hall(hall_type="VIP", price=56)
# hall2 = Hall(hall_type="Regular", price=45)
# scr1 = Screening(movie=movie1, hall=hall1, time=123)
#
# print(scr1.hall.hall_type)
#
# scr1.hall = hall2
#
# print(scr1.hall.hall_type)
#
#
#
#
#
#
# scr1.buy_ticket(3)
# print(scr1.number_of_tickets)
#
#
#
#
#
