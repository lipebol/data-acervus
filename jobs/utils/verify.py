import json


def Verify(directory, items):

    # try:
    with open(f'{directory}/utils/others/jobs.json', 'r') as json_file:
        jobs = json.load(json_file)
    # except (json.decoder.JSONDecodeError):
    dif = []
    if jobs["vagas"] != items["vagas"]:

        json_file = json.dumps(items, ensure_ascii=False, indent=5)
        with open(f'{directory}/utils/others/jobs.json', 'w') as file:
            file.write(json_file)

        
        for item in items["vagas"]:
            if item not in jobs["vagas"]:
                dif.append(item)

        dif_items = {
            "vagas": dif
        }
        
        json_file = json.dumps(dif_items, ensure_ascii=False, indent=5)
        with open(f'{directory}/utils/others/news_jobs.json', 'w') as file:
            file.write(json_file)

    return dif


    