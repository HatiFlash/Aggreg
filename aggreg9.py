# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#j'importe les modules
import feedparser
import time
import datetime
from time import strftime
from datetime import datetime
import yaml

def genere_html(liste_evenements, chemin_html):
    #je récupère l'heure
    date = datetime.now()
    datef=str(date)
    #j'enlève les 19 caractère derrière
    datef=datef[:19]
    listef=[]
    #j'ouvre le fichier html en écriture
    with open (chemin_html, 'w+',encoding='utf-8') as files: 
        #je prépare tout le header et le body
        html_head=['<!DOCTYPE html>','<html lang="en">','<head>',
                   '<meta charset="utf-8">',
                   '<meta name="viewport" content="width=device-width, initial-scale=1">',
                   '<title>Events log</title>',
                   '<link rel="stylesheet" href="style.css" type="text/css"/>',
                   '</head>']
  
        html_body=['<body>','<article>','<header>','<h1>Events log</h1>','</header>',
                   '<p class="heure">',datef,'</p>','</body>']
        
        #je fait une boucle for pour récupérer les informations
        for e in range(len(liste_evenements)-1):
            serveur=liste_evenements[e]['serveur']
            date_pub=liste_evenements[e]['date_publi']
            categorie=liste_evenements[e]['categorie']
            guid=liste_evenements[e]['guid']
            lien=liste_evenements[e]['lien']
            description=liste_evenements[e]['description']
            #ici j'attribu une class en fonction de l'erreur
            if categorie=="MINOR":
                categorie="<p class='minor'>"+categorie
            if categorie=="MAJOR":
                categorie="<p class='major'>"+categorie
            if categorie=="CRITICAL":
                categorie="<p class='critical'>"+categorie
            #je met tout dans une variable sous forme de liste
            article= [
                '<article>','<p class="serveur">','from: '+serveur,'</p>'
                '<p>','pubDate: '+date_pub,'</p>'
                '<p>'+categorie,'</p>'
                '<p>','guid: '+guid,'</p>'
                '<p><a href="{link}">','link: '+lien,'</a></p>'
                '<p>','description: '+description,'</p>','</article>'
                ]
            #j'ajoute à ma listef
            listef.append(article)
        
        #enfin j'écris dans le fichier
        files.writelines(html_head)
        files.writelines(html_body)
        for i in range(len(listef)):
            files.writelines(listef[i])
        
        

      
def fusion_flux(liste_url,liste_flux):
    #j'initialise la liste finale
    final=[]
    dico={}
    #je créer un boucle for pour itérer dans la liste_flux
    for i in range(len(liste_flux)):
        flux=liste_flux[i]
        #vérifie si le flux contient bien quelque chose
        if flux==None:
            print(liste_url[i],"est inaccessible ")
        else:
            #si le fichier est disponible je récupère ce que je veux
            for rss in range(len(flux)):
                #pour obtenir 'tags' je doit rentrer dans plusieurs sous listes
                doc=flux[rss]
                tags2=flux[rss].get('tags')
                dico['titre']=doc.get('title')
                dico['categorie']=tags2[0].get('term')
                serveur=doc.get("link")
                serveur=serveur[7:15]
                dico['serveur']=str(serveur)
                dico['date_publi']=doc.get('published')
                dico['lien']=doc.get('link')
                dico['description']=doc.get('summary')
                dico['guid']=doc.get('guid')
                final.append(dico)
                dico={}
    return(final)


def charges_urls(liste_url):
    #j'initialise la liste finale
    fluxRss=[]
    news_feed=[]
    #je créer un boucle for pour itérer dans la liste_url
    for rss in range(len(liste_url)): 
        #je charge le document rss de la liste_url
        xml=feedparser.parse(liste_url[rss])
        news_feed.append(xml)
	    #vérifie si le documents rss renvoi de l'information ou pas
        if news_feed[rss]["bozo"]==False:
            #si il renvoi rien on ajoute None a la liste
            new=news_feed[rss].get('entries')
            fluxRss.append(new)
        else:
            #sinon on ajoute le document rss a la liste
            fluxRss.append(None)
    #on renvoi la liste des flux
    return(fluxRss)

def recupflux(fichieryaml):
    #j'ouvre le fichier en lecture
    with open(fichieryaml, 'r') as f:
        f=yaml.safe_load(f)
        #je récupère ce dont j'ai besoin (url,nom du fichier,chemin html)
        source= f["sources"]
        files=f["rss-name"]
        html=f["destination"]
        #liste que je vais renvoyer
        listef=[]
        #je fait une boucle for pour mettre le tout dans ma listef
        for i in range(len(source)):
            t=source[i]
            #je combine l'url avec l'extension du fichier
            t+=files
            #je l'ajoute a listef
            listef.append(t)
        #je retourne listef et html
        return(listef,html)

def main():
    source=recupflux("test.yaml")
    html=source[1]
    site=source[0]
    genere_html(fusion_flux(site,charges_urls(site)),html)
if __name__ == "__main__":
    main()
