import subprocess


def Update(directory, dif):

    title = "    Alerta de Vagas    "
    message = f"  Há {len(dif)} nova(s) vaga(s).  "
    # action = "\n   Tecle 'Super + N'  "
    icon = f'--icon={directory}/image/id-card.png'

    command = f'notify-send "{icon}" "{title}" "{message}"'
    subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)