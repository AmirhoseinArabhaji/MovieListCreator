import os
import pickle
from src.movie import Movie


def rename_dir():
    pass


def write_movies_text(movies):
    with open('./movies.txt', 'w') as file:
        for movie in movies:
            try:
                file.write('{} {} {}\n'.format(movie.get_name(), movie.get_year(), movie.get_rate()))
            except:
                file.write("no movie hereeee\n")


def write_movies(movies):
    try:
        with open('./movies.db', 'wb') as file:
            pickle.dump(movies, file)
        print('Writing database successful')
    except:
        print('Error writing database')


def read_movies():
    with open('./movies.db', 'rb') as file:
        movies = pickle.load(file)
        return movies


paths = ['/mnt/d/Movies', '/mnt/g/amir/Movie', '/mnt/g/amir/Drive D', '/mnt/g/amir/New folder']
# paths = ['/mnt/c/Users/Amirhosein/Desktop/New folder (2)'] # test directory
movies = []
try:
    movies = read_movies()
except:
    print('No movies.db found')

for path in paths:
    entries = os.listdir(path)

    # TODO: check for if entry is dir or not
    for entry in entries:
        movie = Movie(entry)
        for item in movies:
            if item.get_original_name() == movie.get_original_name():
                print(entry, 'is in movies.db')
                movie = item
                break
        else:
            print('GETTING:', entry)
            movie.find_info()
            movies.append(movie)

        print('RECIEVED:', movie.get_name())  # TODO remove this line

        if os.path.isdir(path + '/' + entry):
            new_name = movie.get_name().replace(':', '') + ' (' + movie.get_year() + ')'
            if entry != new_name:
                old_path = os.path.join(path, entry)
                new_path = os.path.join(path, new_name)
                try:
                    os.rename(old_path, new_path)
                except:
                    print("rename failed")
movies.sort(key=lambda x: x.get_name().lower())  # sort by name

write_movies(movies)
write_movies_text(movies)

