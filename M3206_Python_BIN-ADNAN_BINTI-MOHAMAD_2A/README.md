# Python
Le projet Python
1. Membres du groupe:
	* BINTI MOHAMAD Nurdini 
	* BIN ADNAN Muhammad Izzat Affandi
	
   Groupe de TP :2 A

2. Avant de commencer, vous devez récuperez tous les fichiers et le mettre dans un dossier.
	Les fichiers importants :
	* log_json.py : Permets de convertir le fichier .log en .json et contient les fonctions pour parser les ligne dans un fichier log.
	* statistique.py : Contient les fonctions qui permettent d'afficher les fenêtres graphiques pour la statistique.
	* graphique.py : affichage de statistique avec des arguments (voyez point 3.iv).
	* apache.log : Exemple d'un fichier de log, au format apache.
	* apache.json : Exemple d'un fichier json (resultat).
	

3. Informations que nous jugons importantes de donner à notre enseignant pour le bon fonctionnement de notre programme :
	
	i. Installez Python 3.9
	
	ii.Faites la commande au dessous pour convertir le fichier apache.log en json :
	
		> python3 log_json.py
		> > Quel fichier log à convertir en json : apache.log
		> > apache.log est bien enregistré en fichier json (apache.json)
		
	iii.Tous les statistiques se fait à partir du fichier apache.json. Pour afficher tous les statistiques possible, fait la commande:
	
		> python3 graphique.py
		
	iv. Pour choisir la statistique spécifique, nous avons utilisé argparse. Les commandes possible sont :
	
		> python3 graphique.py --h : pour afficher tous les commandes possible
		
		> python3 graphique.py --stats os : pour afficher la statistique des systèmes d'exploitation utilisés
		
		> python3 graphique.py --stats reponse : pour afficher la statistique du code renvoyé pour la réponse
		
		> python3 graphique.py --stats heure : pour afficher la statistique des utilisateurs pas heure
		
		> python3 graphique.py --stats ip : pour chercher les informations à partir l'adresse IP
