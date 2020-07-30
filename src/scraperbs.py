import requests
from bs4 import BeautifulSoup

class ScraperBS:
    __headers = {'User-Agent':
                   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    def __init__(self, name, corrected_name=''):
        self.__name = name
        self.__term = name if corrected_name == '' else corrected_name
        self.__movie_title = ''
        self.__movie_year = ''
        self.__movie_rate = ''
        try:
            self.__run()
        except:
            print('ERROR IN GETTING INFO FOR "{}"'.format(self.__term))

    def get_name(self):
        return self.__movie_title if self.__movie_title != '' else self.__name + ' (ERROR GETTING NAME)'

    def get_year(self):
        return self.__movie_year if self.__movie_year != '' else '0000'

    def get_rate(self):
        return self.__movie_rate if self.__movie_rate != '' else '0.0'

    def __get_bing_soup(self):
        url = r'https://www.bing.com/search?q={}&setlang=en-us/'.format(self.__term + ' imdb')
        response = requests.get(url, headers=ScraperBS.__headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def __get_imdb_soup(self):
        url = r'https://www.imdb.com/title/{}/'.format(self.__imdb_id)
        response = requests.get(url, headers=ScraperBS.__headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def __run(self):
        bing_soup = self.__get_bing_soup()
        # results = bing_soup.find('ol', {'id': 'b_results'})
        # headlines = results.find_all('li', {'class': 'b_algo'})
        headlines = bing_soup.find_all('li', {'class': 'b_algo'}) # .find_all('li', class_='b_algo')

        # problem in getting same name movies or tv series like 'snowpiercer'
        for item in headlines:
            # print(i.a.text) # gives title of link
            # print(i.a.string) # gives title of link
            item_text = item.find('a').text # returns the name of link
            item_href = item.find('a').attrs['href'] # returns link of the title
            if 'www.imdb.com/title/' in item_href and 'TV Series' not in item_text:
                # self.__imdb_id = item_href[-10:-1] # gets imdb id of the movie
                self.__imdb_id = item_href[27:-1] # gets imdb id of the movie
                break

        imdb_soup = self.__get_imdb_soup()
        title = imdb_soup.find('div', class_="title_wrapper") # or {'class': 'title_wrapper'} instead of class_='title_wrapper'
        title = title.find('h1').text
        self.__movie_title = title[:-8]
        self.__movie_year = title[-6:-2]
        self.__movie_rate = imdb_soup.find('div', {'class', 'ratingValue'}).text[1:4] # 1 because it has '\n' before rating
