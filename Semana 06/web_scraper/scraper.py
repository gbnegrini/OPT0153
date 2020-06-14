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
        self.soup = None

    def get_html(self, url):
        """Gets the HTML content from a given url"""

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
        """Parses the HTML content with BeautifulSoup."""

        print("Parsing HTML...")
        self.soup = bs4.BeautifulSoup(html.read(), "html.parser")
        print("HTML parsed.")

    def format_seminar(self, article):
        """Formats the scraped data from HTML article tag into the attributes of a Seminar object."""

        seminar = Seminar()
        try:
            seminar.summary = " ".join(article.h2.getText().split()[0:-3])
            seminar.description = article.p.getText() \
                + "\nLink: <" + article.a.get("href") + ">"
            seminar.link = "<" + article.a.get("href") + ">"

            hour_regex = re.compile(r'.\dh')
            minutes_regex = re.compile(r'\d.min')
            date_regex = re.compile(r'.\d/.\d')

            day, month = date_regex.search(
                article.h2.getText()).group().split("/")
            day = int(day)
            if (day < 10):  # If day has only one digit
                # then a zero must be added to match the dateTime template
                day = "0"+str(day)
            day = str(day)

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

            # dateTime template : YYYY-MM-DDTHH:MM:SS-03:00
            seminar.start = str(datetime.today().year)+"-"+month+"-"+day+"T"\
                + hour+":"+minutes+":"+"00"+"-03:00"
            end_hour = str(int(hour)+1)  # Seminars usually last one hour
            seminar.end = str(datetime.today().year)+"-"+month+"-"+day+"T"\
                + end_hour+":"+minutes+":"+"00"+"-03:00"
            return seminar
        except AttributeError:
            print(
                "Error while formatting seminar data. Check HTML for missing tags.")
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(str(traceback.format_exception(exc_type, exc_value, exc_tb)))
            return None

    def log_seminar_data(self, seminar):
        """Prints Seminar object attributes."""

        print("The following seminar was added to the list: ")
        for parameter in seminar.parameters():
            print(parameter)

    def get_seminars(self):
        """Returns a list of Seminar objects based on HTML article tags."""

        articles = self.soup.find_all("article")
        seminars = list()

        for article in articles:
            seminar = format_seminar(article)
            if seminar is not None:
                seminars.append(seminar)
                log_seminar_data(seminar)

        return seminars
