# Block A

def fav_movie():
    fave_movie = input("What's your favorite movie ?: ")
    print(f"{fave_movie} is terrible! How could you like it so much?")

def imdb_rating(rating):
    if rating > 7:
      print("Let's watch it!")
    else:
      print("Not gonna waste my time on that!")
    print("I hope you agree")

def binge(ep_nos):
    for i in range(1,ep_nos):
      print(f"Oh-yeah {i}")
    print(f"There are {len(ep_nos) in the series}")
