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
        """Gets the url HTML content and parses it with BeautifulSoup"""
        print("Getting HTML...")
        try:
            html = urlopen(url)
            print("URL: <" + url + "> opened.")
            self.soup = bs4.BeautifulSoup(html.read(), "html.parser")
            print("HTML parsed.")

        except (HTTPError, URLError) as error:
            print("Error: " + error.__str__())
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(str(traceback.format_exception(exc_type, exc_value, exc_tb)))

    def get_data(self):
        """Does all the magic to extract the seminars information. Returns a list of Seminar objects"""
        try:
            # Gets all <articles> tag
            articles_list = self.soup.find_all("article")

            seminars = []

            for article in articles_list:

                try:
                    seminar_event = Seminar()
                    seminar_event.summary = " ".join(article.h2.getText().split()[0:-3])
                    seminar_event.description = article.p.getText() \
                                                + "\nLink: <" + article.a.get("href") +">"
                    seminar_event.link = "<" + article.a.get("href") +">"

                    # Regex to get hour, minutes and date from the article tag text
                    hour_regex = re.compile(r'.\dh')
                    minutes_regex = re.compile(r'\d.min')
                    date_regex = re.compile(r'.\d/.\d')

                    # Gets the text matching the date regex and splits into day and month
                    day, month = date_regex.search(article.h2.getText()).group().split("/")
                    day = int(day)
                    if (day < 10): # If day has only one digit
                        day = "0"+str(day)  # then a zero must be added to match the dateTime template
                    day = str(day)

                    # Gets the hours matching the hour regex, splits into the "h" delimiter and removes white space
                    hour = hour_regex.search(article.h2.getText()).group().split("h")[0].replace(" ", "")

                    hour = int(hour)
                    if (hour < 10):    # If the hour has only one digit
                        hour = "0"+str(hour)     # then a zero must be added to match the dateTime template

                    hour = str(hour)

                    try:
                        # Gets the minutes matching the minutes regex, splits into the "min" delimiter
                        minutes = minutes_regex.search(article.h2.text).group().split("min")[0]
                    except AttributeError:
                        minutes = "00"      # Sometimes the minutes digits are absent so define it as "00"

                    # dateTime template : YYYY-MM-DDTHH:MM:SS-02:00
                    seminar_event.start = str(datetime.today().year)+"-"+month+"-"+day+"T"\
                                            +hour+":"+minutes+":"+"00"+"-03:00"
                    end_hour = str(int(hour)+1)  # Seminars usually last one hour
                    seminar_event.end = str(datetime.today().year)+"-"+month+"-"+day+"T"\
                                            +end_hour+":"+minutes+":"+"00"+"-03:00"

                    # Adds the seminar object to the seminars list
                    if seminar_event is not None:
                        seminars.append(seminar_event)

                    # Logs the Seminar objects
                    print("The following seminar was added to the list: ")
                    for parameter in seminar_event.parameters():
                        print(parameter)
                except AttributeError:
                    continue

            # Returns the list of Seminar objects that will be used to create the Google Calendar events
            return seminars

        except Exception as error:
            print("Error: " + error.__str__())
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(str(traceback.format_exception(exc_type, exc_value, exc_tb)))
