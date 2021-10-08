#!/usr/bin/python3 
import re
REMOTE_HOSTNAME="^(\d{1,3})\.\d+\.\d+(\.\d+)$"

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
			system_agent=get[5]
		)

def readF(f):
    dictparline=[]
	#ouvrir et parcour par chaque ligne du fichier
    for line in open(f,'r'):
        #enregistrer les infos de chaque ligne dans une liste
        dictparline.append(parse_line(line))
    return dictparline

def get_ip(inputt):
	match=re.search(REMOTE_HOSTNAME,inputt)
	if match:
		# if i found a match
		return match.group(1) 
	return None
	
	

print(readF('apache_logs.log'))
print(get_ip('46.10.14.53'))
