import webbrowser
import requests
import json
from SubirArchivosGitHub import *

#Esta funcion devuelve la tarea de la semana al recibir el numero de semana como parametro
def GetHomework(SemanaN,FilePath):
    #Parte I
    Enalce="https://fpmir.azurewebsites.net/{}/AZFMIR?AZFNUM={}".format("api",SemanaN)
    webbrowser.open(Enalce, new=2)
    #Parte II
    response=requests.get(Enalce).text
    response_info=json.loads(response)
    archivo=open(FilePath, "w")
    json.dump(response_info,archivo,indent=6)
    archivo.close()

InputSemana = input("Ingrese semana:")
InputFile = input("Ingrese\ path y nombre de archivo:")
TokenGithub = input("Ingrese el token: ")
MensajeCommit = input("Ingrese el mensaje para commit: ")
NombreRepo = input("Ingrese el nombre para el repositorio: ")
GetHomework(InputSemana,InputFile)
SubirGitHub(MensajeCommit,TokenGithub,InputFile,NombreRepo)
