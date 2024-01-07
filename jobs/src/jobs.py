from datetime import datetime
from dotenv import find_dotenv, load_dotenv
from json import dumps
from os import environ
from utils.files import pathFile
from utils.notifications import notification
from utils.scrape import scrape


class Jobs:

    load_dotenv(find_dotenv('utils/others/.env'))

    def __init__(self):
        self.__currentHours = datetime.now()
        self.__scrape = scrape()
        self.__HOME = pathFile().directory
        self.__notification = notification(self.__HOME)
        self.__news = ""
        if self.__currentHours.strftime("%A") != "Sunday":
            if self.__currentHours.strftime("%A") == "Saturday" and self.__currentHours.hour > 14:
                exit()
            else:
                if self.__currentHours.hour > 7 and self.__currentHours.hour <= 19:
                    for url in environ.get("URLS").split(","):
                        if 'gupy' in url:
                            self.__news = self.__scrape.gupy(url)
                    self.__jobs = {
                        "vagas": self.__news
                    }
                    self.__json = dumps(self.__jobs, ensure_ascii=False, indent=5)
                    with open(f'{self.__HOME}/utils/others/news_jobs.json', 'w') as file:
                        file.write(self.__json)

                    if len(self.__news) == 0:
                        self.__notification.noUpdate()
                    else:
                        self.__notification.update(self.__news)
                else:
                    exit()
        else:
            exit()

    def run(self):
        return None