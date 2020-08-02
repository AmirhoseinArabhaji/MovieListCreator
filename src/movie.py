from src.scraperbs import ScraperBS
import re

class Movie:
    def __init__(self, name, is_dir=False):
        self.name = name
        self.__corrected_name = self.__correct_name(name)
        self.__scraper = None

    def find_info(self):
        self.__scraper = ScraperBS(self.name, self.__corrected_name)

    def get_original_name(self):
        return self.name

    def get_name(self):
        self.__corrected_name = self.__scraper.get_name()
        return self.__corrected_name

    def get_year(self):
        self.__year = self.__scraper.get_year()
        return self.__year

    def get_rate(self):
        self.__imdb = self.__scraper.get_rate()
        return self.__imdb

    def __correct_name(self, name):
        """
        correct name of the movie by removing the extra characters in the name of file
        """
        # remove useless characters in name of the file
        pattern = r'[\.|_|-|(|)]'
        name = re.sub(pattern, ' ', name)
        # find first occurrence of shown keywords
        pattern = r'(persian)|(remaster)|(proper)|(2160)|(2160p)|(4k)|(480)|(480p)|(720)|(720p)|(1080)|(1080p)|(x265)|(x264)|(brrip)|(bluray)|(director)|(directors)|(directors\-cut)|(10bit)|(10\-bit)|(8bit)|(8\-bit)|(12bit)|(12\-bit)|(dubbed)|(farsi)|(web)|(webdl)|(webrip)|(rip)|(www)|(www\.)|(internal)'
        pattern = re.compile(pattern, re.IGNORECASE)
        match = pattern.search(name)
        # remove extra parts of the name
        index = len(name)
        if match is not None:
            index = match.span()[0]
        result = name[:index]
        return result
