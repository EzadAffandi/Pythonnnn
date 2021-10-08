# !/usr/bin/python3
import re
#la fonction qui permet de détecter l'OS utilisé
def detect_os(systemAgent):
	if 'Windows' in systemAgent:
		return 'Windows'
	if 'Linux' in systemAgent:
		return 'Linux'
	if 'Mac' in systemAgent:
		return 'Mac'
	else:
		return 'unknown'
#la fonction qui permet de séparer les infos dans un ligne
def parse_line(line):
		ip=line.split(' ')
		get=line.split('"')
		
		return dict(
			remote_ip=ip[0],
			time=ip[3]+ip[4],
			request=get[1],
			response=ip[8],
			byte=ip[9],
			referrer=ip[10],
			system_agent=get[5],
			OS=detect_os(get[5])
		)

def readF(f):
    dictparline=[]
	#ouvrir et parcour par chaque ligne du fichier
    for line in open(f,'r'):
        #enregistrer les infos de chaque ligne dans une liste
        dictparline.append(parse_line(line))
    return dictparline
	
print(readF('apache.log'))


