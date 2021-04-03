from scraperbs import ScraperBS
import re


class Movie:
    def __init__(self, name, is_dir=False):
        self.name = name
        self.year = ''
        self.rate = ''
        self.title = ''
        self.corrected_name = self.__correct_name()

    def __str__(self):
        return self.name

    def get_original_name(self):
        return self.name

    def __correct_name(self):
        """
        correct name of the movie by removing the extra characters in the name of file
        """
        # remove useless characters in name of the file
        pattern = r'[\.|_|-|(|)]'
        name = re.sub(pattern, ' ', self.name)
        # find first occurrence of shown keywords
        pattern = r'(persian)|(remaster)|(proper)|(2160)|(2160p)|(4k)|(480)|(480p)|(720)|(720p)|(1080)|(1080p)|(' \
                  r'x265)|(x264)|(brrip)|(bluray)|(director)|(directors)|(directors\-cut)|(10bit)|(10\-bit)|(8bit)|(' \
                  r'8\-bit)|(12bit)|(12\-bit)|(dubbed)|(farsi)|(web)|(webdl)|(webrip)|(rip)|(www)|(www\.)|(internal) '
        pattern = re.compile(pattern, re.IGNORECASE)
        match = pattern.search(name)
        # remove extra parts of the name
        index = len(name)
        if match is not None:
            index = match.span()[0]
        result = name[:index]
        return result
