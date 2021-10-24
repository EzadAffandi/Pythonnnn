from statistique import *
import argparse

parser = argparse.ArgumentParser(description='Convertir fichier log au fichir json') 

# Create the parser 
parser = argparse.ArgumentParser() 

# Add an argument 
parser.add_argument('--stats', type=str,help='les stats possibles: heure, reponse, os, ip') 

# Parse the argument 
args = parser.parse_args() 

if(args.stats==None): 
    statistique_all('apache.json') 
elif(args.stats=='heure'): 
    stat_heure('apache.json') 
elif(args.stats=='reponse'): 
    stat_reponse('apache.json')
elif(args.stats=='os'): 
    stat_OS('apache.json')
elif(args.stats=='ip'): 
    stat_ip('apache.json')
else: 
    print("Seulement heure,reponse ou os") 