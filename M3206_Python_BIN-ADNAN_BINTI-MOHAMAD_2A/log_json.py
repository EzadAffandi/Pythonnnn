#!/usr/bin/python3 
import re
import json
from tkinter import *
import os

# on detecte l'OS utilisé
def detect_os(user_agent):
    if 'Windows' in user_agent:
        return 'Windows'
    if 'Mac OS X 10_9_1' in user_agent:
        return 'Mac OS X'
    if 'iPhone OS 6_0 like Mac OS X' in user_agent:
        return 'iOS 6_0'
    if 'Linux' in user_agent:
        return 'Linux'
    else:
        return 'Unknown'
        
# la fonction qui permet de séparer les infos dans un ligne
def parse_line(line):
        ip=line.split(' ')
        get=line.split('"')
        if(len(ip)>8 and len(get)>4):
           return dict(
			   remote_ip=ip[0],
			   time=ip[3]+" "+ip[4],
			   request=get[1],
			   response=ip[8],
			   bytes=ip[9],
			   referrer=get[3],
			   user_agent=get[5],
               system_agent=detect_os(get[5])
           )

def read_fichier(f):
    dictparline=[]
	#ouvrir et parcour par chaque ligne du fichier
    for line in open(f,'r'):
        #enregistrer les infos de chaque ligne dans une liste
        dictparline.append(parse_line(line))
    
    #ecrit tous les dictionaires dans fichier json
    with open(f[:-4]+'.json','w') as fg:
        json.dump(dictparline, fg, indent=8)
    return dictparline

#demande à l'utilisateur quel fichier il voudrais convertir
def log_to_json():
    fichier1=input('Quel fichier log à convertir en json : ')
    while os.path.isfile(fichier1)==False:
       print(fichier1 + " n'exist pas !")
       fichier1=input('Quel fichier log à convertir en json : ')
    read_fichier(fichier1)
    if os.path.isfile(fichier1[:-4]+".json"):
        print(fichier1 + " est bien enregistré en fichier json (" +fichier1[:-4]+".json)")
log_to_json()
