import subprocess


def noUpdate(directory):

    title = "   Alerta de Vagas   "
    message = "Não há nova(s) vaga(s). "
    icon = f'--icon={directory}/image/id-card.png'

    command = f'notify-send "{icon}" "{title}" "{message}"'
    subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
