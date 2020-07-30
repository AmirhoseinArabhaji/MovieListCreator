import os
from movie import Movie

paths = ['/mnt/d/Movies', '/mnt/g/amir/Movie']
# paths = ['/mnt/c/Users/Amirhosein/Desktop/New folder'] # test directory
movies = []

for path in paths:
    entries = os.listdir(path)
    entries_edited = entries[:]

    for item in entries_edited:
        print('GETTING:', item)
        try:
            movie = Movie(item)
            movies.append(movie)
            print(movie.get_name(), movie.get_year(), movie.get_rate())
        except:
            pass

movies.sort(key=lambda x: x.get_name().lower()) # sort by name

with open('/mnt/c/Users/Amirhosein/Desktop/movies.txt', 'w') as file:
    for i in movies:
        try:
            file.write('{} {} {}\n'.format(i.get_name(), i.get_year(), i.get_rate()))
        except:
            file.write("no movie hereeee\n")
