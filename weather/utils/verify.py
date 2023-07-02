from datetime import datetime
import shutil

def Verify(directory, condition):

    currentHours = datetime.now()
    destination = f'{directory}/image/current/weather.png'

    if currentHours.hour == 6:
        if currentHours.minute >= 14 and currentHours.minute <= 40:
            if condition != "Tempestades isoladas com raios e trovões":
                if condition != "Chuvas com trovoadas":
                    condition = "Nascer do sol"
    if currentHours.hour == 17:
        if currentHours.minute >= 31:
            if condition != "Tempestades isoladas com raios e trovões":
                if condition != "Chuvas com trovoadas":
                    condition = "Pôr do sol"
    if currentHours.hour <= 5 or currentHours.hour >= 18:
        if condition != "Tempestades isoladas com raios e trovões":
            if condition != "Chuvas com trovoadas":
                condition = "Noite"
    
    source = f'{directory}/image/icons/{condition}.png'
    shutil.copyfile(source, destination)