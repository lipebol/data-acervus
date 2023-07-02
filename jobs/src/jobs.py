from utils.files import Files
from utils.notifications.noUpdate import noUpdate
from utils.notifications.update import Update
from utils.scrape import scrapeJobs
from utils.verify import Verify


def Jobs():

    urls, directory = Files()
    local, remote = scrapeJobs(urls)

    jobs = []
    for item in local:
        if item not in remote:
            item = "#Local: " + item + ";\n"
            jobs.append(item)
    
    for item in remote:
        item = "#Remota: " + item + ";\n"
        jobs.append(item)


    items = {
        "vagas": jobs
    }

    dif = Verify(directory, items)

    if len(dif) == 0:
        noUpdate(directory)
    else:
        Update(directory, dif)