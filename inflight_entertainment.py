
def can_two_movies_fill_flight(movie_lengths, flight_length):

    movie_set = set(movie_lengths)
    for movie in movie_set:
        second_film_duration = flight_length - movie
        if second_film_duration in movie_set and second_film_duration is not movie:
            return True
    return False


print(can_two_movies_fill_flight([3, 8, 3], 6))
