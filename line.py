#!/usr/bin/python3 
import re
import json
REMOTE_HOSTNAME="^(\d{1,3})\.\d+\.\d+(\.\d+)$"

#on detecte l'OS utilisé
def detect_os(user_agent):
    if 'Windows NT 6.2' in user_agent:
        return 'Windows NT 6.2'
    if 'Mac OS X' in user_agent:
        return 'Mac OS X'
    if 'Mac OS iPhone OS 6_0X' in user_agent:
        return 'iOS 6_0'
    if 'Linux' in user_agent:
        return 'Linux'
    else:
        return 'unknown'
        
#la fonction qui permet de séparer les infos dans un ligne
def parse_line(line):
		ip=line.split(' ')
		get=line.split('"')
		return dict(
			remote_ip=ip[0],
			time=ip[3]+" "+ip[4],
			request=get[1],
			response=ip[8],
			byte=ip[9],
			referrer=ip[10],
			system_agent=get[5],
            browser_agent=detect_os(get[5])
		)
        

def readFichier(f):
    dictparline=[]
	#ouvrir et parcour par chaque ligne du fichier
    for line in open(f,'r'):
        #enregistrer les infos de chaque ligne dans une liste
        dictparline.append(parse_line(line))
    
    #ecrit tous les dictionaires dans fichier json
    with open(f[:-4]+'.json','w') as fg:
        json.dump(dictparline, fg, indent=8)
    return dictparline

def get_ip(inputt):
	match=re.search(REMOTE_HOSTNAME,inputt)
	if match:
		# if i found a match
		return match.group(1) 
	return None

#print(get_ip('46.10.14.53'))
