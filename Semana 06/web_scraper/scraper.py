from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import bs4
from seminar import Seminar
import re
from datetime import datetime
import traceback
import sys


class WebScraper:

    def __init__(self):
        self.__soup = None

    def get_html(self, url):

        print("Getting HTML...")
        try:
            html = urlopen(url)
            print("HTML from: <" + url + "> retrieved.")
            return html
        except (HTTPError, URLError) as error:
            print(
                "Error while handling HTML retrieval. Check URL and internet connection.")
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(str(traceback.format_exception(exc_type, exc_value, exc_tb)))

    def parse_html(self, html):

        print("Parsing HTML...")
        self.__soup = bs4.BeautifulSoup(html.read(), "html.parser")
        print("HTML parsed.")

    def __format_seminar(self, article):

        seminar = Seminar()
        try:
            seminar = self.__format_text_data(article, seminar)
            month, day = self.__format_date_data(article)
            hour, minutes = self.__format_time_data(article)
            seminar = self.__set_datetime(month, day, hour, minutes, seminar)
            return seminar

        except AttributeError:
            print(
                "Error while formatting seminar data. Check HTML for missing tags.")
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(str(traceback.format_exception(exc_type, exc_value, exc_tb)))
            return None

    def __format_text_data(self, article, seminar):
        seminar.summary = " ".join(article.h2.getText().split()[0:-3])
        seminar.description = article.p.getText() \
            + "\nLink: <" + article.a.get("href") + ">"
        seminar.link = "<" + article.a.get("href") + ">"
        return seminar

    def __format_date_data(self, article):
        date_regex = re.compile(r'.\d/.\d')

        day, month = date_regex.search(
            article.h2.getText()).group().split("/")
        day = int(day)
        if (day < 10):  # If day has only one digit
            # then a zero must be added to match the dateTime template
            day = "0"+str(day)
        day = str(day)
        return month, day

    def __format_time_data(self, article):
        hour_regex = re.compile(r'.\dh')
        minutes_regex = re.compile(r'\d.min')
        hour = hour_regex.search(article.h2.getText()).group().split("h")[
            0].replace(" ", "")
        hour = int(hour)
        if (hour < 10):    # If the hour has only one digit
            # then a zero must be added to match the dateTime template
            hour = "0"+str(hour)
        hour = str(hour)
        try:
            minutes = minutes_regex.search(
                article.h2.text).group().split("min")[0]
        except AttributeError:
            minutes = "00"      # Sometimes the minutes digits are absent so define it as "00"
        return hour, minutes

    def __set_datetime(self, month, day, hour, minutes, seminar):
        # dateTime template : YYYY-MM-DDTHH:MM:SS-03:00
        seminar.start = str(datetime.today().year)+"-"+month+"-"+day+"T"\
            + hour+":"+minutes+":"+"00"+"-03:00"
        end_hour = str(int(hour)+1)  # Seminars usually last one hour
        seminar.end = str(datetime.today().year)+"-"+month+"-"+day+"T"\
            + end_hour+":"+minutes+":"+"00"+"-03:00"
        return seminar

    def __log_seminar_data(self, seminar):

        print("The following seminar was added to the list: ")
        for parameter in seminar.parameters():
            print(parameter)

    def get_seminars(self):

        articles = self.__soup.find_all("article")
        seminars = list()

        for article in articles:
            seminar = self.__format_seminar(article)
            if seminar is not None:
                seminars.append(seminar)
                self.__log_seminar_data(seminar)

        return seminars
