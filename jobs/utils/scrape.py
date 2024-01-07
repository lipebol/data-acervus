from bs4 import BeautifulSoup
from datetime import datetime
from requests import get
from time import sleep
from utils.database import database

class scrape:
    def __init__(self):
        self.__headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"}
        self.__jobs = []
        self.__type_job = 1
        self.__db = database()

    def gupy(self, url):
        self.__url = url
        self.__n = 0
        self.__request = get(
            self.__url,
            headers = self.__headers
        )
        # 'class' do elemento <a>
        self.__gupy = BeautifulSoup(self.__request.text, "lxml").find_all("a", {"class": "sc-a3bd7ea-1 kCVUJf"})
        sleep(20)
        while self.__n < len(self.__gupy):
            self.__uri = self.__gupy[self.__n]['href'].split('?')[0]
            # verificando no "Banco de Dados"
            if self.__db.verify(self.__uri) == 0:
                # dados para o 'news_jobs.json'
                self.__description = self.__gupy[self.__n]['aria-label'].split("Ir para Vaga ")[1].split(". ")[0].split(" publicada em há")[0]
                if " | " in self.__description:
                    self.__description = self.__description.split(" | ")[1]
                self.__job = self.__description + f' - ({self.__uri})'
                if "city" in self.__url:
                    self.__job = "#Local: " + self.__job
                if "workplaceTypes[]=remote" in self.__url:
                    self.__job = "#Remota: " + self.__job
                    self.__type_job = 2
                if self.__job not in self.__jobs:
                    self.__jobs.append(self.__job)
                
                #dados para o 'Banco de Dados' 
                self.__datejob = str(datetime.now()).split(" ")[0]
                self.__company = self.__uri.split("//")[1].split(".gupy.io")[0]
                self.__request = get(
                    self.__uri,
                    headers = self.__headers
                )
                # 'class' do elemento <h1>
                self.__namejob = BeautifulSoup(self.__request.text, "lxml").find("h1", {"class": "sc-673bf470-1 gUHEkj"})
                sleep(10)
                if self.__namejob != None:
                    self.__namejob = self.__namejob.get_text().upper()
                    if " (" in self.__namejob:
                        self.__namejob = self.__namejob.split(" (")[0]
                    if " |" in self.__namejob:
                        self.__namejob = self.__namejob.split(" |")[0]
                    if "| " in self.__namejob:
                        self.__namejob = self.__namejob.split("| ")[0]
                    
                    # inserindo no "Banco de Dados"
                    self.__db.insert(
                        self.__uri, self.__company, self.__namejob, 
                        self.__datejob, self.__type_job
                    )

            self.__n += 1
        
        return self.__jobs
