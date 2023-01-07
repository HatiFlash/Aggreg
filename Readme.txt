CREATE BY SBAI HATIM

Ce manuel vous permet de mettre en place le prgramme python aggreg.py qui permettra de générer des pages html avec tout les flux rss agencé.

Installer aggreg.py sur votre machine:
--------------------------------------

	Déposer le programme aggreg.py ainsi que le fichier flux.yaml dans votre /home
	Déposer le fichier style.css dans /var/www/'nom-de-votre-machine'/

	Installer python3-pip avec la commande : apt install python3-pip
	Installer également les module suivant: 
		feedparser: pip install feedparser
		Yaml: pip install PyYaml

	Allez à l'intérieur du fichier flux.yaml:
		Ajouter vos url des serveurs dans "sources" sous la forme suivante : http://serveur.net/ (veuillez absolument mettre le / a la fin sinon le programme ne fonctionnera pas!)
		Ajouter le nom de votre fichier générer par les serveurs dans "rss-name" sous la forme suivante : rss.xml
		Ajouter le chemin vers votre page html dans "destination" sous la forme suivante : /var/www/'nom-de-votre-machine'/'nom-du-fichier-html'
		Enfin si vous souhaitez avoir un flux trier par ordre chronologique saisissez "True" dans tri-chrono
	
	Avant de continuer tester aggreg.py avec cette commande : python3 aggreg.py
	Si tout s'est bien passer et que le message "ok" s'est affiché passez à la suite sinon aller voir notre FAQ un peu plus bas.

	Une fois cela fait vous devez créer une commande crontab pour éxécuter le programme en boucle pour avoir votre site en temps réel:
		faite : crontab -e
		Sélectionner : 1
		insérez la commande suivante (en respectant bien les espaces): * * * * * Python3 aggreg.py
	
	Voila votre programme est prêt! 
	Rendez-vous sur votre site avec votre machine client est entrer l'url de votre aggreg.

FAQ:
----
Quand je fait "Python3 aggreg.py" j'ai un message d'erreur qui me dit que le fichier n'existe pas ?
-vérifier que vous êtes bien a l'endroit ou vous avez déposer votre fichier, si c'est le cas faite la commande "ls" pour vérifier que le fichier est bien présent.
-Si le fichier n'est pas présent cela veux dire que vous l'avez mal importer sur votre machine.
-Pour rappel la commande pour importer un fichier vers une machine est la suivante: scp aggreg.py aggreg@ip(mettre l'ip de l'aggreg):

Quand je fait "Python3 aggreg.py" j'ai un message d'erreur qui me dit "commande non reconnu"?
-C'est probablement car python3 n'est pas installer sur votre machine, faite le avec cette commande: sudo apt install python3

Quand je lance le programme aggreg.py j'ai un message quie me dit "http://serveur... ,est inaccessible"?
-Cela veux dire que l'url renseigné dans le fichier yaml est soit incorrect, où bien que votre serveur est actuellement inaccessible/indisponible.

Mon crontab ne fonctionne pas?
-Cela doit être car vous n'avez pas mis le chemin exact où se trouve votre fichier aggreg.py.
-Pour savoir quel est le chemin exact rendez-vous là où se trouve le fichier et taper la commande: pwd
-Puis ajouter ce chemin à votre crontab et réessayer.