movies = {
    "War": [3, 5],
    "Bourne": [18, 5],
    "Gully boy": [15, 5],
    "Uri": [12, 5]
}

movie_name = input("Enter movie name: ")
age = int(input("Enter your age: "))

if movie_name in movies:
    min_age = movies[movie_name][0]
    seats = movies[movie_name][1]

    if age >= min_age:
        if seats > 0:
            print("You are eligible to watch the movie.")
            print("Ticket available. Enjoy the show!")
        else:
            print("Sorry, tickets are sold out.")
    else:
        print("You are not eligible to watch this movie.")
else:
    print("Movie not available in the cinema.")
