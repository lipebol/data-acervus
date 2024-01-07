from subprocess import run, PIPE

class notification:
    def __init__(self, HOME):
        self.__directory = HOME
        self.__title = "    Alerta de Vagas    "
        self.__icon = f'--icon={self.__directory}/image/id-card.png'

    def update(self, newsjobs):
        self.__news = newsjobs
        self.__message = f"  Há {len(self.__news)} nova(s) vaga(s).  "
        run(
            f'notify-send "{self.__icon}" "{self.__title}" "{self.__message}"',
            shell=True, stdout=PIPE, text=True
        )

    def noUpdate(self):
        self.__message = "Não há nova(s) vaga(s). "
        run(
            f'notify-send "{self.__icon}" "{self.__title}" "{self.__message}"', 
            shell=True, stdout=PIPE, text=True
        )
