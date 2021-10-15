import re
import json
from tkinter import *
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
			referrer=get[3],
			user_agent=get[5],
            system_agent=detect_os(get[5])
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
    alert_popup("Coucou", "C'est fait !", "Vous trouverez le fichier json à apache.json")
    return dictparline
def statsReponse(data):
	ok=0
	error=0
	for i in data:
		if i['response']=='200':
			ok=ok+1
		if i['response']=='404':
			error=error+1
	return dict(ok=ok,error=error)
def get_ip(inputt):
	match=re.search(REMOTE_HOSTNAME,inputt)
	if match:
		# if i found a match
		return match.group(1) 
	return None
def alert_popup(title, message, path):
    """Generate a pop-up window for special messages."""
    root = Tk()
    root.title(title)
    w = 400     # popup window width
    h = 200     # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = message
    m += '\n'
    m += path
    w = Label(root, text=m, width=120, height=10)
    w.pack()
    b = Button(root, text="OK", command=root.destroy, width=10)
    b.pack()
    mainloop()
li='83.149.9.216 - - [17/May/2015:10:05:03 +0000] "GET /presentations/logstash-monitorama-2013/images/kibana-search.png HTTP/1.1" 200 203023 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"'
final=readFichier('apache.txt')
