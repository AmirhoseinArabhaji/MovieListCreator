import os
import pickle
import threading
from movie import Movie
from scraperbs import ScraperBS


def rename_dir():
    pass


def write_movies_text(movies):
    """
    write movies in a text file
    """
    with open('./movies.txt', 'w') as file:
        for movie in movies:
            try:
                file.write(f'{movie.title} {movie.year} {movie.rate}\n')
            except:
                file.write("no movie hereeee\n")


def write_movies_db(movies):
    """
    write movies in database
    """
    try:
        with open('./movies.db', 'wb') as file:
            pickle.dump(movies, file)
        print('Writing database successful')
    except:
        print('Error writing database')


def read_movies():
    """
    read movies from database
    """
    with open('./movies.db', 'rb') as file:
        movies = pickle.load(file)
        return movies


def find_info(movie):
    print(movie.name)
    scraper = ScraperBS(movie.name, movie.corrected_name)
    movie.title = scraper.get_name()
    movie.year = scraper.get_year()
    movie.rate = scraper.get_rate()
    movies.append(movie)
    print(movie.title, movie.year, movie.rate)
    # return movie


paths = ['D:\\Movies']
# paths = ['C:\\Users\\Amirhosein\\Desktop\\New folder']
movies = []
threads = []


def main():
    # try:
    #     movies = read_movies()
    # except:
    #     print('No movies.db found')

    for path in paths:
        entries = os.listdir(path)

        # TODO: check for if entry is dir or not
        # every file and folder in path
        for entry in entries:
            # create object from entry name
            movie = Movie(entry)

            t = threading.Thread(target=find_info, args=(movie,))
            t.start()
            threads.append(t)

            # if os.path.isdir(path + '/' + entry):
            #     new_name = movie.get_name().replace(':', '') + ' (' + movie.get_year() + ')'
            #     if entry != new_name:
            #         old_path = os.path.join(path, entry)
            #         new_path = os.path.join(path, new_name)
            #         try:
            #             os.rename(old_path, new_path)
            #         except:
            #             print("rename failed")

    # wait for threads to finish
    for t in threads:
        t.join()

    # sort by an attribute of an object
    movies.sort(key=lambda x: x.title.lower())  # sort by name

    # write_movies_db(movies)
    write_movies_text(movies)


if __name__ == '__main__':
    main()
