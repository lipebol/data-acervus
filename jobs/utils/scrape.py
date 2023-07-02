import requests
from bs4 import BeautifulSoup
import time


def scrapeJobs(urls):

    local = []
    remote = []
    for url in urls:
        headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"}
        r = requests.get(
            url, 
            headers = headers,
        )
        soup = BeautifulSoup(r.text, "lxml")
        # 'class' do elemento <a>
        a = soup.find_all("a", {"class": "sc-70b75bd4-1 blwed"})
        time.sleep(10)
        n = 0
        while n < len(a):
            uri = a[n]['href'].split('?')[0]
            description = a[n]['aria-label'].split("Ir para Vaga ")[1]
            description = description.split(". ")[0].split(" publicada em há")[0]
            item = description + f' - ({uri})'
            if "|" in description:
                description = description.split(" | ")[1]
            if "city" in url:
                if description not in local:
                    local.append(item)
            if "remoteWorking" in url:
                if description not in remote:
                    remote.append(item)
                         
            n += 1

    return local, remote