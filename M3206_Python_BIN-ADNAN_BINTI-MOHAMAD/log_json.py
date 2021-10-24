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

def cherche_OS(liste): 
    #créé la liste pour compter les OS utilisé
    data={'Windows':0,'Mac OS X':0,'iOS 6_0':0,'Linux':0,'Unknown':0}
    
    #on traverse dans la tableau pour chercher le system_agent utilisé et le comparer
    for i in liste:
        if i['system_agent']=='Windows' :
            #data[0] est pour compter le system_agent de Windows
            data['Windows']=data['Windows']+1
        if i['system_agent']=='Mac OS X' :
            #data[1] est pour compter le system_agent de Mac OS X
            data['Mac OS X']=data['Mac OS X']+1
        if i['system_agent']=='iOS 6_0':
            #data[2] est pour compter le system_agent de iOS 6_0X
            data['iOS 6_0']=data['iOS 6_0']+1
        if i['system_agent']=='Linux':
            #data[3] est pour compter le system_agent de Linux
            data['Linux']=data['Linux']+1
        if i['system_agent']=='Unknown':
            data['Unknown']=data['Unknown']+1
    return data

def cherche_heure(dictionaire):
    heure={'00':0,'01':0,'02':0,'03':0,'04':0,'05':0,'06':0,'07':0,'08':0,'09':0,'10':0,'11':0,'12':0,'13':0,'14':0,'15':0,'16':0,'17':0,'18':0,'19':0,'20':0,'21':0,'22':0,'23':0} 
    j=0
    for i in dictionaire: 
       j=j+1 
       for hour in heure: 
           tab=i['time'].split(':') 
           if(tab[1]==hour): 
              heure[hour]=heure[hour]+1 
    return heure

#convertir le fichier log en json
read_fichier('apache.log')

#demande à l'utilisateur quel fichier il voudrais convertir
def main():
    fichier1=input('Quel fichier log à convertir en json : ')
    while os.path.isfile(fichier1)==False:
       print(fichier1 + " n'exist pas !")
       fichier1=input('Quel fichier log à convertir en json : ')
    read_fichier(fichier1)
    if os.path.isfile(fichier1[:-4]+".json"):
        print(fichier1 + " est bien enregistré en fichier json (" +fichier1[:-4]+".json)")