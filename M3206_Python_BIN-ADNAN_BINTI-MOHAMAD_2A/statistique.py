#!/usr/bin/python3 
import re
import json
from tkinter import *
import os

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

#les statistiques	
def statistique_all(f):
    #lecture
    with open(f,'r') as fg:
        # returne JSON objet comme dictionaire
        dictionaire = json.load(fg)
    
    #on compte chaque OS utilisé
    data=cherche_OS(dictionaire) 
            
    #On cherche la totale de tous les datas récuperés
    total=len(dictionaire)
   
    for j in data:
        data[j]=data[j]/total*100
        
    #Création d'un objet "fenêtre"
    fenetre = Tk()
    # Affichage du titre
    fenetre.title("Statistique du fichier "+f)

    c = Canvas(fenetre, width=1700, height=800, background="black")
    c.pack(expand=True)
    
    #graphe bar pour OS
    c.create_rectangle(20, 110, 700, 500, fill="white")
    x1=120
    x2=180
    y2=450
    c.create_text(350, 150, text="La statistique des systèmes d'exploitation utilisés", fill="red")
    for i in data:
        c.create_rectangle(x1, 4.5*(100-data[i]), x2, y2, fill="#1E90FF", outline="#1E90FF")
        c.create_text(x1+30, 460, text=i, fill="black")
        c.create_text(x1+30, 4.5*(100-data[i])-20, text=str(data[i])+"%", fill="black")
        x1=x1+100
        x2=x2+100
   
    #ligne verticale
    c.create_line(70, 150, 70, 470,fill="red")
    #ligne horizontale
    c.create_line(40, 450, 650, 450,fill="red")

	#afficher la taille de fichier
    file_size = int(os.path.getsize(f)/1024/1024)
    c.create_rectangle(70, 10, 320, 90, fill="grey30")
    c.create_text(190, 40, text="La taille de "+f+" :", fill="white")
    c.create_text(190, 60, text=str(file_size) + " Mo", fill="white")
   
    #afficher code de reponse
    ok=0
    error=0
    total=0
    totalbit=0
    not_valide=0
    for i in dictionaire:
        total=total+1
        if i['response']=='200':
            ok=ok+1
            if(i['bytes']!='-'):
                totalbit=totalbit+int(i['bytes'])
        if i['response']=='404':
            error=error+1
            not_valide=not_valide+1
            
    ok=(ok/total)*360
    error=(error/total)*360
    other=360-ok-error

    c.create_rectangle(750, 110, 1450, 500, fill="white")
    c.create_text(1280, 150, text="La statistique du code renvoyé pour la réponse", fill="red")
    c.create_arc((850,150,1150,450),fill="green yellow",outline="green yellow",start=0,extent=ok)
    c.create_arc((850,150,1150,450),fill="blue",outline="blue",start=ok,extent=error)
    c.create_arc((850,150,1150,450),fill="yellow",outline="yellow",start=ok+error,extent=other)
    #les symboles de couleur
    c.create_rectangle(1200, 230, 1230, 260, fill="green yellow",outline="green yellow")
    c.create_text(1270, 240, text="200 OK")
    c.create_rectangle(1200, 280, 1230, 310, fill="blue",outline="blue")
    c.create_text(1300, 290, text="404 BAD REQUEST")
    c.create_rectangle(1200, 330, 1230, 360, fill="yellow",outline="yellow")
    c.create_text(1270, 340, text="Autre")
	
	#afficher le nombre de reponse valide
    c.create_rectangle(350, 10, 570, 90, fill="grey30")
    c.create_text(460, 40, text="La réponse 200 OK :", fill="white")
    c.create_text(460, 60, text=str(round(totalbit, -6)/1000000) + " Mbits", fill="white")
    
    #afficher totale requete valide
    c.create_rectangle(620, 10, 840, 90, fill="grey30")
    c.create_text(740, 40, text="Totale requête  :", fill="white")
    c.create_text(740, 60, text=total, fill="white")
    
    #afficher totale requete 
    c.create_rectangle(890, 10, 1110, 90, fill="grey30")
    c.create_text(1000, 40, text="Valide requête  :", fill="white")
    c.create_text(1000, 60, text=total-not_valide, fill="white")
    
    #compte les referrers
    list_ref=[]
    for i['referrer'] in dictionaire:
            if i['referrer'] not in list_ref:
                list_ref.append(i['referrer'])
    #afficher la nombre de referrer 
    c.create_rectangle(1160, 10, 1380, 90, fill="grey30")
    c.create_text(1270, 40, text="Total referrer défini :", fill="white")
    c.create_text(1270, 60, text=len(list_ref), fill="white")
    
    #afficher les statistique par heure
    heure=cherche_heure(dictionaire)
    k=0
    
    c.create_rectangle(20, 520, 1450, 800, fill="white")
    for h in heure: 
      i=heure[h] 
      c.create_rectangle(80+(50*k), 798-i/2, 120+(50*k), 770 , fill="salmon", outline="salmon") 
      c.create_text(80+(50*k)+24, 798-i/2-15,text=i) 
      c.create_text(80+(50*k)+24, 778,text=h+'h') 
      k=k+1    
    c.create_text(700, 795, text="La statistique des utilisateurs par heure", fill="red")      
 
    #Démarrage de la boucle Tkinter (à placer à la fin !!!)
    fenetre.mainloop()
    
def stat_OS(f):
    #lecture
    with open(f,'r') as fg:
        # returne JSON objet comme dictionaire
        dictionaire = json.load(fg)
        
    #on compte chaque OS utilisé
    data=cherche_OS(dictionaire)
    #On cherche la totale de tous les datas récuperés
    total=len(dictionaire)
    
    for j in data:
        data[j]=data[j]/total*100
        
    #Création d'un objet "fenêtre"
    fenetre = Tk()
    # Affichage du titre
    fenetre.title("Statistique du fichier "+f)

    c = Canvas(fenetre, width=600, height=600)
    c.pack(expand=True)
    
    #graphe bar pour OS
    x1=60
    x2=120
    y2=450
    c.create_text(300, 50, text="La statistique des systèmes d'exploitation utilisés", fill="red")
    for i in data:
        c.create_rectangle(x1, 4.5*(100-data[i]), x2, y2, fill="#1E90FF", outline="#1E90FF")
        c.create_text(x1+30, 460, text=i, fill="black")
        c.create_text(x1+30, 4.5*(100-data[i])-20, text=str(data[i])+"%", fill="black")
        x1=x1+100
        x2=x2+100
        
    #ligne verticale
    c.create_line(50, 150, 50, 470,fill="red")
    #ligne horizontale
    c.create_line(40, 450, 550, 450,fill="red")
    fenetre.mainloop()
    
def stat_reponse(f):
    #lecture
    with open(f,'r') as fg:
        # returne JSON objet comme dictionaire
        dictionaire = json.load(fg)
    
    #Création d'un objet "fenêtre"
    fenetre = Tk()
    # Affichage du titre
    fenetre.title("Statistique du fichier "+f)

    c = Canvas(fenetre, width=600, height=600)
    c.pack(expand=True)
    
    #afficher code de reponse
    ok=0
    error=0
    total=0
    totalbit=0
    not_valide=0
    for i in dictionaire:
        total=total+1
        if i['response']=='200':
            ok=ok+1
            if(i['bytes']!='-'):
                totalbit=totalbit+int(i['bytes'])
        if i['response']=='404':
            error=error+1
            not_valide=not_valide+1
			
    ok=(ok/total)*360
    error=(error/total)*360
    other=360-ok-error

    c.create_text(300, 50, text="La statistique du code renvoyé pour la réponse", fill="red")
    c.create_arc((50,100,300,350),fill="green yellow",outline="green yellow",start=0,extent=ok)
    c.create_arc((50,100,300,350),fill="blue",outline="blue",start=ok,extent=error)
    c.create_arc((50,100,300,350),fill="yellow",outline="yellow",start=ok+error,extent=other)
    #les symboles de couleur
    c.create_rectangle(370, 150, 400, 180, fill="green yellow",outline="green yellow")
    c.create_text(430, 165, text="200 OK")
    c.create_rectangle(370, 190, 400, 220, fill="blue",outline="blue")
    c.create_text(460, 205, text="404 BAD REQUEST")
    c.create_rectangle(370, 230, 400, 260, fill="yellow",outline="yellow")
    c.create_text(430, 245, text="Autre")
    
    #Démarrage de la boucle Tkinter (à placer à la fin !!!)
    fenetre.mainloop()
    
def stat_heure(f):
    #lecture
    with open(f,'r') as fg:
        # returne JSON objet comme dictionaire
        dictionaire = json.load(fg)
    
    heure=cherche_heure(dictionaire)
    root = Tk() 

    root.title("Les statistiques des requêtes en heure")  

    c_width = 1220 
    c_height = 350 
    c = Canvas(root, width=c_width, height=c_height) 
    c.pack() 

    x1=10 
    x2=20 
    k=0 
    c.create_text(600, 20, text="La statistique des utilisateurs par heure", fill="red")  
    for h in heure: 
      i=heure[h] 
      c.create_rectangle(10+(50*k), 335-i/2, 60+(50*k), 338 , fill="salmon") 
      c.create_text(10+(50*k)+24, 335-i/2-15,text=i) 
      c.create_text(10+(50*k)+24, 345,text=h+'h') 
      k=k+1 

    root.mainloop() 


def stat_ip(f):
    
    def get_ip():
        #lecture
        with open('apache.json','r') as fg:
            # returne JSON objet comme dictionaire
            dictionaire = json.load(fg)
            
        ip = entrer_ip.get()
        entrer_ip.delete(0, END)
        data_ip=[]
        for requete in dictionaire:
            if requete['remote_ip']==ip:
                data_ip.append(requete)
        
        #on compte chaque OS utilisé
        os_utilise=cherche_OS(data_ip)
        
        #cherche le code 200 
        ok=0
        for i in data_ip:
            if i['response']=='200':
                ok=ok+1
        
        #Création d'un objet "fenêtre"
        fenetre = Tk()
        # Affichage du titre
        fenetre.title(ip)
        
        c = Canvas(fenetre, width=1000, height=500)
        c.pack(expand=True)
        
        if len(data_ip)==0:
            #fenetre.destroy()
            c.create_text(250, 40, text="L'adresse IP cherché n'existe pas. Veuillez chercher un autre adresse !")
        else:
            #ligne verticale
            c.create_rectangle(10, 80, 10*len(data_ip), 110, fill="#1E90FF", outline="#1E90FF")
            c.create_text(10*len(data_ip)+50, 95, text="Total requête ("+str(len(data_ip))+")")
            c.create_rectangle(10, 120, 10*ok, 150, fill="#1020F6", outline="#1020F6")
            c.create_text(10*ok+40, 135, text="200 OK ("+str(ok)+")")
        
            #afficher les reslutat d'OS utilisé
            y1=160
            y2=190
            for i in os_utilise:
                if os_utilise[i] != 0:
                    c.create_rectangle(10, y1, 10*os_utilise[i], y2, fill="#1E900F", outline="#1E900F")
                    c.create_text(10*os_utilise[i]+50, y1+15, text=str(i)+" ("+str(os_utilise[i])+")")
                    y1=y1+50
                    y2=y2+50
              
            c.create_line(10, 50, 10, 450,fill="red")
            
        
        #Démarrage de la boucle Tkinter (à placer à la fin !!!)
        fenetre.mainloop()
        
    rt = Tk()
    rt.title("Cherche des informations avec l'adresse IP")
    rt.geometry('500x100')
   
    entrer_ip = Entry(rt, width = 15)
    entrer_ip.pack()
    Button(rt, text='Cherche', command=get_ip).pack()
    rt.mainloop()