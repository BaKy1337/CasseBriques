from tkinter import * #Le programme va aller chercher toute les fonctions de la bibliothèque Tkinter
import math,random    #Le programme va aller chercher toute les fonctions de la bibliotèque math
from math import cos,pi,sin
from winsound import *
import sys
import threading as th
from time import time, sleep
from tkinter.messagebox import *

fenetre= Tk()
fenetre.title("Casse briques")

#-----Fonction "Clavier" : binds pour la raquette-----#
def Clavier(event):#Fonction pour bouger raquette
    """ Gestion de l'événement Appui sur une touche du clavier """
    global x1,x2,raquette,vitesse,PAUSE,FLAG,PAUPER
    touche = event.keysym
    #Déplacement vers la droite
    if PAUPER==1:#Si on a pas perdu
        if PAUPER!=0:#Si on ne vient pas de perdre
            if P==2:#Si P=2 alors le jeu est lancé
                if PAUSE !=0:#Si le jeu n'est pas sur pause
                    if Perdu !=1: #Si on ne vient pas de perdre
                        Can1.delete(raquette)
                        if touche == 'Right' and x2<=549:
                            x1 += 13.5333333333
                            x2 += 13.5333333333
                        ###Déplacement vers la gauche###
                        if touche == 'Left' and x1>=0.4:
                            x1 -= 13.5333333333
                            x2 -= 13.5333333333
                        #On donne les nouvelles coordonnées à la raquette
                        Can1.coords(raquette,x1,y1,x2,y2)
                        raquette=Can1.create_image(x1+72,y1-15,image=RAQUETTE)
                    if Perdu==1:#Pour bouger quand on vient de mourrir
                        if PAUSE !=0:#Si le jeu n'est pas sur pause
                            Can1.delete(raquette)
                        if touche == 'Right' and x2<=549:
                            x1 += 13.5333333333
                            x2 += 13.5333333333
                        ###Déplacement vers la gauche###
                        if touche == 'Left' and x1>=0.4:
                            x1 -= 13.5333333333
                            x2 -= 13.5333333333
                        #On donne les nouvelles coordonnées à la raquette
                        Can1.coords(raquette,x1,y1,x2,y2)
                        raquette=Can1.create_image(x1+72,y1-15,image=RAQUETTE)

#-----Fonction "quitter" : quitter le jeu-----#
def quitter (event):#Pour quitter le programme
    fenetre.destroy()
    NoSound= PlaySound(None, SND_PURGE)

#-----Fonction "pleinecran" : affichage en fullscreen-----#
def pleinecran (event):
    global Pleine,w,h
    if Pleine==0:
        fenetre.geometry("750x600+0+0")
        fenetre.overrideredirect(0)
        Pleine=1
    else:
        w, h = fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()
        fenetre.overrideredirect(1)
        fenetre.geometry("%dx%d+0+0" % (w, h))
        Pleine=0
        
#-----Fonction "déplacement" : déplacements de la balle, -----#
def deplacement():
    """ Déplacement de la balle """
    global X,Y,DX,DY,RAYON,LARGEUR,HAUTEUR,FLAG,x1,x2,y1,y2,vitesse,cible2,PAUSE,P,Perdu,PAUPER,imagepause,nbrvie,score,Scoretext,count,score,high,highscoretext
    global Imagevie33,Imagevie22,Imagevie11,Brique,Brique1,Brique2,Brique3,Brique4,Brique5,Brique6,Brique7,Brique8,Brique9,Brique10
    global Brique11,Brique12,Brique13,Brique14,Brique15,Brique16,Brique17,C,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,C14,C15,C16,C17
    global BLOCK0,BLOCK1,BLOCK2,BLOCK3,BLOCK4,BLOCK5,BLOCK6,BLOCK7,BLOCK8,BLOCK9,BLOCK10,BLOCK11,BLOCK12,BLOCK13,BLOCK14,BLOCK15
    global BLOCK16,BLOCK17,I0,I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12,I13,I14,I15,I16,I17,timer
    
    Can2.delete(Scoretext)
    Scoretext = Can2.create_text(100,400, text="SCORE:"+str(score),font=("Fixedsys Normal",24),fill='white')
    if high <= score:
            high=score
            Can2.delete(highscoretext)
            highscoretext= Can2.create_text(100,300, text="Highscore:"+str(high),font=("Fixedsys Normal",20),fill='white')
    #Réinitialise le highscore à chaque fois 
    
    P=2
    Can1.delete(cible2)
    # Déplacement de la balle et rebonds sur les bords et briques
    #Rebond à droite
    if X+RAYON+DX > LARGEUR:
        X = 2*(LARGEUR-RAYON)-X
        DX = -DX
    #Rebond à gauche
    if X-RAYON+DX < 0:
        X = 2*RAYON-X
        DX = -DX
    #Rebond en bas
    if Y+RAYON+DY > HAUTEUR:
        Y = 2*(HAUTEUR-RAYON)-Y
        DY = -DY   
    #Rebond en haut
    if Y-RAYON+DY < 0:
        Y = 2*RAYON-Y
        DY = -DY
        
    X = X+DX
    Y = Y+DY
    
    if C==1 and C==1 and C1==1 and C2==1 and C3==1 and C4==1 and C5==1 and C6==1 and C7==1 and C8==1 and C9==1 and C10==1 and C11==1 and C12==1 and C13==1 and C14==1 and C15==1 and C16==1 and C17==1:
        count=46
        Gameover1=1
        timer=1
        PAUPER=2
        Can2.delete(Temps)
        timer=1 #Prépare variable pour relance le chrono
        Can2.delete(Scoretext)
        Scoretext = Can2.create_text(100,400, text="SCORE:"+str(score),font=("Fixedsys Normal",24),fill='white')

        if C==1:
            BLOCK0= PhotoImage(file='image/blockhead.gif')
            I0=Can1.create_image(75,75,image=BLOCK0)
            C=0 
        if C1==1:
            BLOCK1= PhotoImage(file='image/blockhead.gif')
            I1=Can1.create_image(175,75,image=BLOCK1)
            C1=0
        if C2==1:
            BLOCK2= PhotoImage(file='image/blockhead.gif')
            I2=Can1.create_image(275,75,image=BLOCK2)
            C2=0
        if C3==1:
            BLOCK3= PhotoImage(file='image/blockhead.gif')
            I3=Can1.create_image(375,75,image=BLOCK3)
            C3=0
        if C4==1:
            BLOCK4= PhotoImage(file='image/blockhead.gif')
            I4=Can1.create_image(475,75,image=BLOCK4)
            C4=0
        if C5==1:
            BLOCK5= PhotoImage(file='image/blockhead.gif')
            I5=Can1.create_image(125,125,image=BLOCK5)
            C5=0
        if C6==1:
            BLOCK6= PhotoImage(file='image/blockhead.gif')
            I6=Can1.create_image(225,125,image=BLOCK6)
            C6=0
        if C7==1:
            BLOCK7= PhotoImage(file='image/blockhead.gif')
            I7=Can1.create_image(325,125,image=BLOCK7)
            C7=0
        if C8==1:
            BLOCK8= PhotoImage(file='image/blockhead.gif')
            I8=Can1.create_image(425,125,image=BLOCK8)
            C8=0
        if C9==1:
            BLOCK9= PhotoImage(file='image/blockhead.gif')
            I9=Can1.create_image(75,225,image=BLOCK9)
            C9=0
        if C10==1:
            BLOCK10= PhotoImage(file='image/blockhead.gif')
            I10=Can1.create_image(125,225,image=BLOCK10)
            C10=0
        if C11==1:
            BLOCK11= PhotoImage(file='image/blockhead.gif')
            I11=Can1.create_image(175,225,image=BLOCK11)
            C11=0
        if C12==1:
            BLOCK12= PhotoImage(file='image/blockhead.gif')
            I12=Can1.create_image(225,225,image=BLOCK12)
            C12=0
        if C13==1:
            BLOCK13= PhotoImage(file='image/blockhead.gif')
            I13=Can1.create_image(275,225,image=BLOCK13)
            C13=0
        if C14==1:
            BLOCK14= PhotoImage(file='image/blockhead.gif')
            I14=Can1.create_image(325,225,image=BLOCK14)
            C14=0
        if C15==1:
            BLOCK15= PhotoImage(file='image/blockhead.gif')
            I15=Can1.create_image(375,225,image=BLOCK15)
            C15=0
        if C16==1:
            BLOCK16= PhotoImage(file='image/blockhead.gif')
            I16=Can1.create_image(425,225,image=BLOCK16)
            C16=0
        if C17==1:
            BLOCK17= PhotoImage(file='image/blockhead.gif')
            I17=Can1.create_image(475,225,image=BLOCK17)
            C17=0
        showinfo("GAGNE","Vous avez gagné !")
        PAUPER=1
        Gameover1=1
        stop()
        RAYON = 10 #Rayon de la balle
        X = LARGEUR/2 #
        Y = 535 #Pour la mettre au dessus de la raquette qui est à 560pixels
        P=2 #La balle se met en mouvement
        FLAG=0 #Vitesse de la balle nulle
        Perdu=1
        PAUPER=1
        imagepause=0 #Empêche le gif "pause" de s'afficher
        
        if high <= score:
            high=score
            Can2.delete(highscoretext)
            highscoretext= Can2.create_text(100,300, text="Highscore:"+str(high),font=("Fixedsys Normal",20),fill='white')
        
        Can1.coords(Balle,X-RAYON,Y-RAYON,X+RAYON,Y+RAYON)

    if C!=1:
        if 50<=X+RAYON<=60:
            if 50<=Y<=100:
                DX=-DX
                C=1
                score=score+100
                Can1.delete(fenetre,Brique)
                BLOCK0=0
        if 90<=X-RAYON<=100:
            if 50<=Y<=100:
                DX=-DX
                C=1
                score=score+100
                Can1.delete(fenetre,Brique)
                BLOCK0=0
        if 90<=Y-RAYON<=100:
            if 50<=X<=100:
                DY=-DY
                C=1
                score=score+100
                Can1.delete(fenetre,Brique)
                BLOCK0=0
        if 50<=Y+RAYON<=60:
            if 50<=X<=100:
                DY=-DY
                C=1
                score=score+100
                Can1.delete(fenetre,Brique)
                BLOCK0=0
    if C1!=1: 
        if 150<=X+RAYON<=160:
            if 50<=Y<=100:
                DX=-DX
                C1=1
                score=score+100
                Can1.delete(fenetre,Brique1)
                BLOCK1=0
        if 190<=X-RAYON<=200:
            if 50<=Y<=100:
                DX=-DX
                C1=1
                score=score+100
                Can1.delete(fenetre,Brique1)
                BLOCK1=0
        if 90<=Y-RAYON<=100:
            if 150<=X<=200:
                DY=-DY
                C1=1
                score=score+100
                Can1.delete(fenetre,Brique1)
                BLOCK1=0
        if 50<=Y+RAYON<=60:
            if 150<=X<=200:
                DY=-DY
                C1=1
                score=score+100
                Can1.delete(fenetre,Brique1)
                BLOCK1=0      
    if C2!=1: 
        if 250<=X+RAYON<=260:
            if 50<=Y<=100:
                DX=-DX
                C2=1
                score=score+100
                Can1.delete(fenetre,Brique2)
                BLOCK2=0
        if 290<=X-RAYON<=300:
            if 50<=Y<=100:
                DX=-DX
                C2=1
                score=score+100
                Can1.delete(fenetre,Brique2)
                BLOCK2=0
        if 90<=Y-RAYON<=100:
            if 250<=X<=300:
                DY=-DY
                C2=1
                score=score+100
                Can1.delete(fenetre,Brique2)
                BLOCK2=0
        if 50<=Y+RAYON<=60:
            if 250<=X<=300:
                DY=-DY
                C2=1
                score=score+100
                Can1.delete(fenetre,Brique2)
                BLOCK2=0
            
    if C3!=1: 
        if 350<=X+RAYON<=360:
            if 50<=Y<=100:
                DX=-DX
                C3=1
                score=score+100
                Can1.delete(fenetre,Brique3)
                BLOCK3=0
        if 390<=X-RAYON<=400:
            if 50<=Y<=100:
                DX=-DX
                C3=1
                score=score+100
                Can1.delete(fenetre,Brique3)
                BLOCK3=0
        if 90<=Y-RAYON<=100:
            if 350<=X<=400:
                DY=-DY
                C3=1
                score=score+100
                Can1.delete(fenetre,Brique3)
                BLOCK3=0
        if 50<=Y+RAYON<=60:
            if 350<=X<=400:
                DY=-DY
                C3=1
                score=score+100
                Can1.delete(fenetre,Brique3)
                BLOCK3=0
    if C4!=1: 
        if 450<=X+RAYON<=460:
            if 50<=Y<=100:
                DX=-DX
                C4=1
                score=score+100
                Can1.delete(fenetre,Brique4)
                BLOCK4=0
        if 490<=X-RAYON<=500:
            if 50<=Y<=100:
                DX=-DX
                C4=1
                score=score+100
                Can1.delete(fenetre,Brique4)
                BLOCK4=0
        if 90<=Y-RAYON<=100:
            if 450<=X<=500:
                DY=-DY
                C4=1
                score=score+100
                Can1.delete(fenetre,Brique4)
                BLOCK4=0
        if 50<=Y+RAYON<=60:
            if 450<=X<=500:
                DY=-DY
                C4=1
                score=score+100
                Can1.delete(fenetre,Brique4)
                BLOCK4=0
    if C5!=1: 
        if 100<=X+RAYON<=110:
            if 100<=Y<=150:
                DX=-DX
                C5=1
                score=score+100
                Can1.delete(fenetre,Brique5)
                BLOCK5=0
        if 140<=X-RAYON<=150:
            if 100<=Y<=150:
                DX=-DX
                C5=1
                score=score+100
                Can1.delete(fenetre,Brique5)
                BLOCK5=0
        if 140<=Y-RAYON<=150:
            if 100<=X<=150:
                DY=-DY
                C5=1
                score=score+100
                Can1.delete(fenetre,Brique5)
                BLOCK5=0
        if 100<=Y+RAYON<=110:
            if 100<=X<=150:
                DY=-DY
                C5=1
                score=score+100
                Can1.delete(fenetre,Brique5)
                BLOCK5=0
    if C6!=1: 
        if 200<=X+RAYON<=210:
            if 100<=Y<=150:
                DX=-DX
                C6=1
                score=score+100
                Can1.delete(fenetre,Brique6)
                BLOCK6=0
        if 240<=X-RAYON<=250:
            if 100<=Y<=150:
                DX=-DX
                C6=1
                score=score+100
                Can1.delete(fenetre,Brique6)
                BLOCK6=0
        if 140<=Y-RAYON<=150:
            if 200<=X<=250:
                DY=-DY
                C6=1
                score=score+100
                Can1.delete(fenetre,Brique6)
                BLOCK6=0
        if 100<=Y+RAYON<=110:
            if 200<=X<=250:
                DY=-DY
                C6=1
                score=score+100
                Can1.delete(fenetre,Brique6)
                BLOCK6=0
    if C7!=1: 
        if 300<=X+RAYON<=310:
            if 100<=Y<=150:
                DX=-DX
                C7=1
                score=score+100
                Can1.delete(fenetre,Brique7)
                BLOCK7=0
        if 340<=X-RAYON<=350:
            if 100<=Y<=150:
                DX=-DX
                C7=1
                score=score+100
                Can1.delete(fenetre,Brique7)
                BLOCK7=0
        if 140<=Y-RAYON<=150:
            if 300<=X<=350:
                DY=-DY
                C7=1
                score=score+100
                Can1.delete(fenetre,Brique7)
                BLOCK7=0
        if 100<=Y+RAYON<=110:
            if 300<=X<=350:
                DY=-DY
                C7=1
                score=score+100
                Can1.delete(fenetre,Brique7)
                BLOCK7=0
    if C8!=1: 
        if 400<=X+RAYON<=410:
            if 100<=Y<=150:
                DX=-DX
                C8=1
                score=score+100
                Can1.delete(fenetre,Brique8)
                BLOCK8=0
        if 440<=X-RAYON<=450:
            if 100<=Y<=150:
                DX=-DX
                C8=1
                score=score+100
                Can1.delete(fenetre,Brique8)
                BLOCK8=0
        if 140<=Y-RAYON<=150:
            if 400<=X<=450:
                DY=-DY
                C8=1
                score=score+100
                Can1.delete(fenetre,Brique8)
                BLOCK8=0
        if 100<=Y+RAYON<=110:
            if 400<=X<=450:
                DY=-DY
                C8=1
                score=score+100
                Can1.delete(fenetre,Brique8)
                BLOCK8=0
    if C9!=1: 
        if 50<=X+RAYON<=60:
            if 200<=Y<=250:
                DX=-DX
                C9=1
                score=score+100
                Can1.delete(fenetre,Brique9)
                BLOCK9=0
        if 90<=X-RAYON<=100:
            if 200<=Y<=250:
                DX=-DX
                C9=1
                score=score+100
                Can1.delete(fenetre,Brique9)
                BLOCK9=0
        if 240<=Y-RAYON<=250:
            if 50<=X<=100:
                DY=-DY
                C9=1
                score=score+100
                Can1.delete(fenetre,Brique9)
                BLOCK9=0
        if 200<=Y+RAYON<=210:
            if 50<=X<=100:
                DY=-DY
                C9=1
                score=score+100
                Can1.delete(fenetre,Brique9)
                BLOCK9=0
    if C10!=1: 
        if 100<=X+RAYON<=110:
            if 200<=Y<=250:
                DX=-DX
                C10=1
                score=score+100
                Can1.delete(fenetre,Brique10)
                BLOCK10=0
        if 140<=X-RAYON<=150:
            if 200<=Y<=250:
                DX=-DX
                C10=1
                score=score+100
                Can1.delete(fenetre,Brique10)
                BLOCK10=0
        if 240<=Y-RAYON<=250:
            if 100<=X<=150:
                DY=-DY
                C10=1
                score=score+100
                Can1.delete(fenetre,Brique10)
                BLOCK10=0
        if 200<=Y+RAYON<=210:
            if 100<=X<=150:
                DY=-DY
                C10=1
                score=score+100
                Can1.delete(fenetre,Brique10)
                BLOCK10=0
    if C11!=1: 
        if 150<=X+RAYON<=160:
            if 200<=Y<=250:
                DX=-DX
                C11=1
                score=score+100
                Can1.delete(fenetre,Brique11)
                BLOCK11=0
        if 190<=X-RAYON<=200:
            if 200<=Y<=250:
                DX=-DX
                C11=1
                score=score+100
                Can1.delete(fenetre,Brique11)
                BLOCK11=0
        if 240<=Y-RAYON<=250:
            if 150<=X<=200:
                DY=-DY
                C11=1
                score=score+100
                Can1.delete(fenetre,Brique11)
                BLOCK11=0
        if 200<=Y+RAYON<=210:
            if 150<=X<=200:
                DY=-DY
                C11=1
                score=score+100
                Can1.delete(fenetre,Brique11)
                BLOCK11=0
    if C12!=1: 
        if 200<=X+RAYON<=210:
            if 200<=Y<=250:
                DX=-DX
                C12=1
                score=score+100
                Can1.delete(fenetre,Brique12)
                BLOCK12=0
        if 240<=X-RAYON<=250:
            if 200<=Y<=250:
                DX=-DX
                C12=1
                score=score+100
                Can1.delete(fenetre,Brique12)
                BLOCK12=0
        if 240<=Y-RAYON<=250:
            if 200<=X<=250:
                DY=-DY
                C12=1
                score=score+100
                Can1.delete(fenetre,Brique12)
                BLOCK12=0
        if 200<=Y+RAYON<=210:
            if 200<=X<=250:
                DY=-DY
                C12=1
                score=score+100
                Can1.delete(fenetre,Brique12)
                BLOCK12=0
    if C13!=1: 
        if 250<=X+RAYON<=260:
            if 200<=Y<=250:
                DX=-DX
                C13=1
                score=score+100
                Can1.delete(fenetre,Brique13)
                BLOCK13=0
        if 290<=X-RAYON<=300:
            if 200<=Y<=250:
                DX=-DX
                C13=1
                score=score+100
                Can1.delete(fenetre,Brique13)
                BLOCK13=0
        if 240<=Y-RAYON<=250:
            if 250<=X<=300:
                DY=-DY
                C13=1
                score=score+100
                Can1.delete(fenetre,Brique13)
                BLOCK13=0
        if 200<=Y+RAYON<=210:
            if 250<=X<=300:
                DY=-DY
                C13=1
                score=score+100
                Can1.delete(fenetre,Brique13)
                BLOCK13=0
    if C14!=1: 
        if 300<=X+RAYON<=310:
            if 200<=Y<=250:
                DX=-DX
                C14=1
                score=score+100
                Can1.delete(fenetre,Brique14)
                BLOCK14=0
        if 340<=X-RAYON<=350:
            if 200<=Y<=250:
                DX=-DX
                C14=1
                score=score+100
                Can1.delete(fenetre,Brique14)
                BLOCK14=0
        if 240<=Y-RAYON<=250:
            if 300<=X<=350:
                DY=-DY
                C14=1
                score=score+100
                Can1.delete(fenetre,Brique14)
                BLOCK14=0
        if 200<=Y+RAYON<=210:
            if 300<=X<=350:
                DY=-DY
                C14=1
                score=score+100
                Can1.delete(fenetre,Brique14)
                BLOCK14=0
    if C15!=1: 
        if 350<=X+RAYON<=360:
            if 200<=Y<=250:
                DX=-DX
                C15=1
                score=score+100
                Can1.delete(fenetre,Brique15)
                BLOCK15=0
        if 390<=X-RAYON<=400:
            if 200<=Y<=250:
                DX=-DX
                C15=1
                score=score+100
                Can1.delete(fenetre,Brique15)
                BLOCK15=0
        if 240<=Y-RAYON<=250:
            if 350<=X<=400:
                DY=-DY
                C15=1
                score=score+100
                Can1.delete(fenetre,Brique15)
                BLOCK15=0
        if 200<=Y+RAYON<=210:
            if 350<=X<=400:
                DY=-DY
                C15=1
                score=score+100
                Can1.delete(fenetre,Brique15)
                BLOCK15=0
    if C16!=1: 
        if 400<=X+RAYON<=410:
            if 200<=Y<=250:
                DX=-DX
                C16=1
                score=score+100
                Can1.delete(fenetre,Brique16)
                BLOCK16=0
        if 440<=X-RAYON<=450:
            if 200<=Y<=250:
                DX=-DX
                C16=1
                score=score+100
                Can1.delete(fenetre,Brique16)
                BLOCK16=0
        if 240<=Y-RAYON<=250:
            if 400<=X<=450:
                DY=-DY
                C16=1
                score=score+100
                Can1.delete(fenetre,Brique16)
                BLOCK16=0
        if 200<=Y+RAYON<=210:
            if 400<=X<=450:
                DY=-DY
                C16=1
                score=score+100
                Can1.delete(fenetre,Brique16)
                BLOCK16=0
    if C17!=1: 
        if 450<=X+RAYON<=460:
            if 200<=Y<=250:
                DX=-DX
                C17=1
                score=score+100
                Can1.delete(fenetre,Brique17)
                BLOCK17=0
        if 490<=X-RAYON<=500:
            if 200<=Y<=250:
                DX=-DX
                C17=1
                score=score+100
                Can1.delete(fenetre,Brique17)
                BLOCK17=0
        if 240<=Y-RAYON<=250:
            if 450<=X<=500:
                DY=-DY
                C17=1
                score=score+100
                Can1.delete(fenetre,Brique17)
                BLOCK17=0
        if 200<=Y+RAYON<=210:
            if 450<=X<=500:
                DY=-DY
                C17=1
                score=score+100
                Can1.delete(fenetre,Brique17)
                BLOCK17=0
                
#Si la balle tape la barre
    if Y+RAYON >= y2 and x1 <= X <= x2 :
        DY = -DY
        #x1 le côté gauche de la raquette et x2 le côté droit
        #Côté gauche de la raquette
        if x1-1 < X < x1+20: # "X" est la coordonnée de la balle
            DX = vitesse*math.cos(5*pi/6)
        if x1+20 < X < x1+42: 
            DX = vitesse*math.cos(3*pi/4)
        if x1+42 < X < x1+63: 
            DX = vitesse*math.cos(2*pi/3)
        if x1+63 < X < x1+68:
            DX = vitesse*math.cos(7*pi/12)

#Rebonds sur les côtés de la raquette
        #Côté droit de la raquette
        if x2-68 < X < x2-63:
            DX = vitesse*math.cos(5*pi/12)
        if x2-63 < X < x2-42: 
            DX = vitesse*math.cos(pi/3)
        if x2-42 < X < x2-20:
            DX = vitesse*math.cos(pi/4)
        if x2-20 < X < x2+1:
            DX = vitesse*math.cos(pi/6)
#Ici l'angle prend un angle droit à cause de cos de pi/2
        if x1+68 < X < x1+88:
            DX = vitesse*math.cos(pi/2)        

    if Y >= y2 and x1+RAYON >= X+RAYON >= x1:
        X = 2*(LARGEUR-RAYON)-X
        
    if Y >= y2 and x2-RAYON <= X-RAYON <= x2:
        X = 2*(LARGEUR-RAYON)-X
    
    if Y > 600:#Quand la balle va en dessous de l'écran
        stop()
        RAYON = 10 #Rayon de la balle
        X = LARGEUR/2 #
        Y = 535 #Pour la mettre au dessus de la raquette qui est à 560pixels
        P=2 #La balle se met en mouvement
        FLAG=0 #Vitesse de la balle nulle
        Perdu=1 #
        PAUPER=1
        imagepause=0 #Empêche le gif "pause" de s'afficher
        nbrvie=nbrvie-1
        
        Can1.coords(Balle,X-RAYON,Y-RAYON,X+RAYON,Y+RAYON)

#-----Système de vies-----#
        if nbrvie==2:
            Imagevie33=0
        if nbrvie==1:
            Imagevie22=0
        if nbrvie==0:
            Imagevie11=0
        if nbrvie==-1:
            #On réinitialise le nombre de vies après le game over ainsi que le score
            if high <= score:
                high=score
                Can2.delete(highscoretext)
                highscoretext= Can2.create_text(100,300, text="Highscore:"+str(high),font=("Fixedsys Normal",20),fill='white')
            score=0
            count=46
            Gameover1=1
            timer=1
            PAUPER=2
            Can2.delete(Temps)
            timer=1 #Prépare variable pour relance le chrono
            Can2.delete(Scoretext)
            Scoretext = Can2.create_text(100,400, text="SCORE:"+str(score),font=("Fixedsys Normal",24),fill='white')
            nbrvie=3
            Imagevie11= PhotoImage(file='image/vie.gif')
            Imagevie1=Can2.create_image(50,100,image=Imagevie11)

            Imagevie22= PhotoImage(file='image/vie.gif')
            Imagevie2=Can2.create_image(100,100,image=Imagevie22)

            Imagevie33= PhotoImage(file='image/vie.gif')
            Imagevie3=Can2.create_image(150,100,image=Imagevie33)

            if C==1:
                BLOCK0= PhotoImage(file='image/blockhead.gif')
                I0=Can1.create_image(75,75,image=BLOCK0)
                C=0 
            if C1==1:
                BLOCK1= PhotoImage(file='image/blockhead.gif')
                I1=Can1.create_image(175,75,image=BLOCK1)
                C1=0
            if C2==1:
                BLOCK2= PhotoImage(file='image/blockhead.gif')
                I2=Can1.create_image(275,75,image=BLOCK2)
                C2=0
            if C3==1:
                BLOCK3= PhotoImage(file='image/blockhead.gif')
                I3=Can1.create_image(375,75,image=BLOCK3)
                C3=0
            if C4==1:
                BLOCK4= PhotoImage(file='image/blockhead.gif')
                I4=Can1.create_image(475,75,image=BLOCK4)
                C4=0
            if C5==1:
                BLOCK5= PhotoImage(file='image/blockhead.gif')
                I5=Can1.create_image(125,125,image=BLOCK5)
                C5=0
            if C6==1:
                BLOCK6= PhotoImage(file='image/blockhead.gif')
                I6=Can1.create_image(225,125,image=BLOCK6)
                C6=0
            if C7==1:
                BLOCK7= PhotoImage(file='image/blockhead.gif')
                I7=Can1.create_image(325,125,image=BLOCK7)
                C7=0
            if C8==1:
                BLOCK8= PhotoImage(file='image/blockhead.gif')
                I8=Can1.create_image(425,125,image=BLOCK8)
                C8=0
            if C9==1:
                BLOCK9= PhotoImage(file='image/blockhead.gif')
                I9=Can1.create_image(75,225,image=BLOCK9)
                C9=0
            if C10==1:
                BLOCK10= PhotoImage(file='image/blockhead.gif')
                I10=Can1.create_image(125,225,image=BLOCK10)
                C10=0
            if C11==1:
                BLOCK11= PhotoImage(file='image/blockhead.gif')
                I11=Can1.create_image(175,225,image=BLOCK11)
                C11=0
            if C12==1:
                BLOCK12= PhotoImage(file='image/blockhead.gif')
                I12=Can1.create_image(225,225,image=BLOCK12)
                C12=0
            if C13==1:
                BLOCK13= PhotoImage(file='image/blockhead.gif')
                I13=Can1.create_image(275,225,image=BLOCK13)
                C13=0
            if C14==1:
                BLOCK14= PhotoImage(file='image/blockhead.gif')
                I14=Can1.create_image(325,225,image=BLOCK14)
                C14=0
            if C15==1:
                BLOCK15= PhotoImage(file='image/blockhead.gif')
                I15=Can1.create_image(375,225,image=BLOCK15)
                C15=0
            if C16==1:
                BLOCK16= PhotoImage(file='image/blockhead.gif')
                I16=Can1.create_image(425,225,image=BLOCK16)
                C16=0
            if C17==1:
                BLOCK17= PhotoImage(file='image/blockhead.gif')
                I17=Can1.create_image(475,225,image=BLOCK17)
                C17=0
            showinfo("PERDU","Vous avez perdu !")
            PAUPER=1
            Gameover1=0

#-----Affichage de la balle-----#
    Can1.coords(Balle,X-RAYON,Y-RAYON,X+RAYON,Y+RAYON)
    

    if FLAG >0:
        fenetre.after(30,deplacement) #Mise à jour toutes les 30 ms
    cible2=Can1.create_image(X,Y,image=dbz)

#-----Fonction stop [arrêt du jeu]-----#
def stop():
    "arret de l'animation"
    global FLAG
    FLAG =0

#-----Fonction start [démarrage du jeu]-----#
def start(event): #On met event pour pouvoir executer la fonction grâce à la touche entrer
#Démarrage de l'animation
 global FLAG,instructions,P,Perdu,PAUPER,Gameover1,timer,count
 if P==3:#Premier lancement
     instructions=0 #On enlève l'image instructions
     if FLAG ==0:  #Pour ne lancer qu’une seule boucle
         FLAG =1
         deplacement()
         P=2
         PAUSE=0
         PAUPER=1
         Gameover1=0
         th_1.start()#Lance timer
         th_2.start()#Lance timer
 if  Perdu==1:
     if PAUPER==1:
         Gameover1=0
         P=2
         FLAG =1
         deplacement()
         Perdu=0
         if timer!= 0:
             timer=0
             count=46
                         
 if P==3:#Premier lancement
     instructions=0 #On enlève l'image instructions
     if FLAG ==0:  #Pour ne lancer qu’une seule boucle
         FLAG =1
         deplacement()
         P=2
         PAUSE=0
         PAUPER=1
         Gameover1=0
         th_1.start()#Lance timer
         th_2.start()#Lance timer
 if P==1:
     instructions=0 #On enlève l'image instructions
     if FLAG ==0:  #Pour ne lancer qu’une seule boucle
         P=2
         FLAG =1
         deplacement()
                         
#-----Fonction pause-----#   
def pause(event):
    global PAUSE,text,FLAG,cible3,imagepause,P,PAUPER,REPAUSE
    if P==2:#Si le jeu à démarrer comme ça impossible de faire pause avant de jouer
        if Perdu!=1:#Si aucun point n'est perdu
            if PAUSE==0:#Si on est pas sur pause
                if Perdu==0:
                    imagepause=''#on fait disparaitre l'image une fois que l'utilisateur à appuyé sur p
                    FLAG=1#On met flag=1 qui est un parametre nécessaire pour lancer le programme
                    deplacement()#On lance le programme
                    PAUPER=1#Pauper a besoin d'être égal à 1 pour bouger la raquette
                    PAUSE=1#On met pause=1 pour préparer la fonction la prochaine fois que l'utilisateur press p
                    musique_menu = PlaySound("musique/Formula1.wav",SND_ASYNC)
            else:
                while PAUSE!=0:
                    if PAUSE==1:#Si la fonction pause est activée
                        imagepause= PhotoImage(file='image/pause.gif')
                        cible3=Can1.create_image(275,250,image=imagepause)#On affiche l'image 
                        stop()#On arrête le jeu
                        PAUSE=0
                        PAUPER=2#Si Pauper=2, la raquette ne peut plus bouger
                        NoSound= PlaySound(None, SND_PURGE)
        
    if Perdu==1:#Si la balle atteint le fond
        if imagepause!=0:#Si l'image est affichée
#-----Faire disparaître l'image-----#
            imagepause=0#On fait disparaitre l'image une fois que l'utilisateur à appuyé sur p
            PAUPER=1#La raquette peut bouger
            REPAUSE=0
            musique_menu = PlaySound("musique/Formula1.wav",SND_ASYNC)
            
        if REPAUSE==1:
            imagepause= PhotoImage(file='image/pause.gif')
            cible3=Can1.create_image(275,250,image=imagepause)#On affiche l'image
            stop()#On arrête le jeu
            PAUSE=1#Fonction pause activée
            PAUPER=2#La raquette ne peut plus bouger
            NoSound= PlaySound(None, SND_PURGE)
        REPAUSE=1
        
def countdown():
    global Temps,Scoretext,nbrvie,score,P,FLAG,Perdu,PAUPER,RAYON,X,Y,count,timer,Gameover1,nul,high,highscoretext,score
    global Imagevie33,Imagevie22,Imagevie11,Brique,Brique1,Brique2,Brique3,Brique4,Brique5,Brique6,Brique7,Brique8,Brique9,Brique10
    global Brique11,Brique12,Brique13,Brique14,Brique15,Brique16,Brique17,C,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,C14,C15,C16,C17
    global BLOCK0,BLOCK1,BLOCK2,BLOCK3,BLOCK4,BLOCK5,BLOCK6,BLOCK7,BLOCK8,BLOCK9,BLOCK10,BLOCK11,BLOCK12,BLOCK13,BLOCK14,BLOCK15
    global BLOCK16,BLOCK17,I0,I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12,I13,I14,I15,I16,I17
    start = time()
    while count!=0:
        count = 46
        while Gameover1!=1:
            while timer==0:
                while PAUPER!=2:
                    count -= 1
                    Temps = Can2.create_text(100,450, text="TEMPS:"+str(count),font=("Fixedsys Normal",24),fill='white')
                    sleep(1)
                    Can2.delete(Temps)
                    nul=0
                    if count==0: #si count=0 alors on sort des boucles grâce aux conditions puis réinitialise les paramètre du programme pour tout remettre à zéro.
                        timer=1
                        Gameover1=1
                        PAUPER=2

    while nul !=0:
        nul=nul+1
        Can1.coords(Balle,X-RAYON,Y-RAYON,X+RAYON,Y+RAYON)

    PAUPER=1
    Gameover1=0
    #On met les conditions qui fait que la partie est perdue pour tout remettre à zéro
    timer=1
    PAUPER=1
    Gameover1=1
    stop()
    X = LARGEUR/2 #
    Y = 535 #Pour la mettre au dessus de la raquette qui est à 560pixels
    P=2 #La balle se met en mouvement
    FLAG=0 #Vitesse de la balle nulle
    Perdu=1 #
    PAUPER=1
    imagepause=0 #Empêche le gif "pause" de s'afficher
        
    Can1.coords(Balle,X-RAYON,Y-RAYON,X+RAYON,Y+RAYON)

    if high <= score:
        high=score
        Can2.delete(highscoretext)
        highscoretext= Can2.create_text(100,300, text="Highscore:"+str(high),font=("Fixedsys Normal",20),fill='white')
    
    score=0
    Can2.delete(Scoretext)
    nbrvie=3
    nul=1
    
    Imagevie11= PhotoImage(file='image/vie.gif')
    Imagevie1=Can2.create_image(50,100,image=Imagevie11)

    Imagevie22= PhotoImage(file='image/vie.gif')
    Imagevie2=Can2.create_image(100,100,image=Imagevie22)

    Imagevie33= PhotoImage(file='image/vie.gif')
    Imagevie3=Can2.create_image(150,100,image=Imagevie33)

    if C==1:
        BLOCK0= PhotoImage(file='image/blockhead.gif')
        I0=Can1.create_image(75,75,image=BLOCK0)
        C=0 
    if C1==1:
        BLOCK1= PhotoImage(file='image/blockhead.gif')
        I1=Can1.create_image(175,75,image=BLOCK1)
        C1=0
    if C2==1:
        BLOCK2= PhotoImage(file='image/blockhead.gif')
        I2=Can1.create_image(275,75,image=BLOCK2)
        C2=0
    if C3==1:
        BLOCK3= PhotoImage(file='image/blockhead.gif')
        I3=Can1.create_image(375,75,image=BLOCK3)
        C3=0
    if C4==1:
        BLOCK4= PhotoImage(file='image/blockhead.gif')
        I4=Can1.create_image(475,75,image=BLOCK4)
        C4=0
    if C5==1:
        BLOCK5= PhotoImage(file='image/blockhead.gif')
        I5=Can1.create_image(125,125,image=BLOCK5)
        C5=0
    if C6==1:
        BLOCK6= PhotoImage(file='image/blockhead.gif')
        I6=Can1.create_image(225,125,image=BLOCK6)
        C6=0
    if C7==1:
        BLOCK7= PhotoImage(file='image/blockhead.gif')
        I7=Can1.create_image(325,125,image=BLOCK7)
        C7=0
    if C8==1:
        BLOCK8= PhotoImage(file='image/blockhead.gif')
        I8=Can1.create_image(425,125,image=BLOCK8)
        C8=0
    if C9==1:
        BLOCK9= PhotoImage(file='image/blockhead.gif')
        I9=Can1.create_image(75,225,image=BLOCK9)
        C9=0
    if C10==1:
        BLOCK10= PhotoImage(file='image/blockhead.gif')
        I10=Can1.create_image(125,225,image=BLOCK10)
        C10=0
    if C11==1:
        BLOCK11= PhotoImage(file='image/blockhead.gif')
        I11=Can1.create_image(175,225,image=BLOCK11)
        C11=0
    if C12==1:
        BLOCK12= PhotoImage(file='image/blockhead.gif')
        I12=Can1.create_image(225,225,image=BLOCK12)
        C12=0
    if C13==1:
        BLOCK13= PhotoImage(file='image/blockhead.gif')
        I13=Can1.create_image(275,225,image=BLOCK13)
        C13=0
    if C14==1:
        BLOCK14= PhotoImage(file='image/blockhead.gif')
        I14=Can1.create_image(325,225,image=BLOCK14)
        C14=0
    if C15==1:
        BLOCK15= PhotoImage(file='image/blockhead.gif')
        I15=Can1.create_image(375,225,image=BLOCK15)
        C15=0
    if C16==1:
        BLOCK16= PhotoImage(file='image/blockhead.gif')
        I16=Can1.create_image(425,225,image=BLOCK16)
        C16=0
    if C17==1:
        BLOCK17= PhotoImage(file='image/blockhead.gif')
        I17=Can1.create_image(475,225,image=BLOCK17)
        C17=0

    showinfo("PERDU","Vous avez perdu !")
    if Gameover1==1:
        count=46
        countdown()
        

def affichage():
    global timer,count
    while count==0:
        sleep(1)
                     
#-----DEBUT DU PROGRAMME-----#
Canfond =Canvas

Can1 = Canvas(fenetre, width=550, height=600, highlightthickness=0)
Can1.pack(side=LEFT)                                

LARGEUR =550 #Largeur de la fenêtre
HAUTEUR = 700 #Hauteur de la fenêtre
BG= PhotoImage (file='image/backg.gif')
bg=Can1.create_image(275,300,image=BG)

#-----Canevas 2 : affichage du score et des vies-----#

Can2 = Canvas(fenetre, width=200,height=600,bg='black')
Can2.pack(side=LEFT)
BG2= PhotoImage (file='image/can2.gif')
bg=Can2.create_image(102,300,image=BG2)

#-----Rectangle : affichage-----#
x1 = ((1/3)*LARGEUR)+20
y1 = 590 
x2 =  ((2/3)*LARGEUR)-20 
y2 = 560

RAQUETTE= PhotoImage(file='image/RAQUETTE.gif')
raquette=Can1.create_image(x1+72,y1-15,image=RAQUETTE)
Can1.focus_set()
Can1.bind('<Key>',Clavier)

#-----Balle : coordonnées-----#
RAYON = 10 
X = LARGEUR/2 
Y = 535 

#-----Déplacement de la balle : coordonnées aléatoires initiales-----#
angle = random.uniform(0,2*math.pi)
vitesse = random.uniform(1.8,2)*5
DX = vitesse*math.cos(2/pi)
DY = vitesse*math.sin(angle) 
dbz= PhotoImage (file='image/BALLE.gif')
FLAG=0

#-----Balle : affichage-----#
Balle = Can1.create_oval(X-RAYON,Y-RAYON,X+RAYON,Y+RAYON,width=1,fill='orange')
cible2=Can1.create_image(X,Y,image=dbz)

#-----Briques : affichage-----#
Brique=Can1.create_rectangle(50,50,100,100)
C=0
BLOCK0= PhotoImage(file='image/blockhead.gif')
I0=Can1.create_image(75,75,image=BLOCK0)

Brique1=Can1.create_rectangle(150,50,200,100)
C1=0
BLOCK1= PhotoImage(file='image/blockhead.gif')
I1=Can1.create_image(175,75,image=BLOCK1)

Brique2=Can1.create_rectangle(250,50,300,100)
C2=0
BLOCK2= PhotoImage(file='image/blockhead.gif')
I2=Can1.create_image(275,75,image=BLOCK2)

Brique3=Can1.create_rectangle(350,50,400,100)
C3=0
BLOCK3= PhotoImage(file='image/blockhead.gif')
I3=Can1.create_image(375,75,image=BLOCK3)

Brique4=Can1.create_rectangle(450,50,500,100)
C4=0
BLOCK4= PhotoImage(file='image/blockhead.gif')
I4=Can1.create_image(475,75,image=BLOCK4)

Brique5=Can1.create_rectangle(100,100,150,150)
C5=0
BLOCK5= PhotoImage(file='image/blockhead.gif')
I5=Can1.create_image(125,125,image=BLOCK5)

Brique6=Can1.create_rectangle(200,100,250,150)
C6=0
BLOCK6= PhotoImage(file='image/blockhead.gif')
I6=Can1.create_image(225,125,image=BLOCK6)

Brique7=Can1.create_rectangle(300,100,350,150)
C7=0
BLOCK7= PhotoImage(file='image/blockhead.gif')
I7=Can1.create_image(325,125,image=BLOCK7)

Brique8=Can1.create_rectangle(400,100,450,150)
C8=0
BLOCK8= PhotoImage(file='image/blockhead.gif')
I8=Can1.create_image(425,125,image=BLOCK8)

Brique9=Can1.create_rectangle(50,200,100,250)
C9=0
BLOCK9= PhotoImage(file='image/blockhead.gif')
I9=Can1.create_image(75,225,image=BLOCK9)

Brique10=Can1.create_rectangle(100,200,150,250)
C10=0
BLOCK10= PhotoImage(file='image/blockhead.gif')
I10=Can1.create_image(125,225,image=BLOCK10)

Brique11=Can1.create_rectangle(150,200,200,250)
C11=0
BLOCK11= PhotoImage(file='image/blockhead.gif')
I11=Can1.create_image(175,225,image=BLOCK11)

Brique12=Can1.create_rectangle(200,200,250,250)
C12=0
BLOCK12= PhotoImage(file='image/blockhead.gif')
I12=Can1.create_image(225,225,image=BLOCK12)

Brique13=Can1.create_rectangle(250,200,300,250)
C13=0
BLOCK13= PhotoImage(file='image/blockhead.gif')
I13=Can1.create_image(275,225,image=BLOCK13)

Brique14=Can1.create_rectangle(300,200,350,250)
C14=0
BLOCK14= PhotoImage(file='image/blockhead.gif')
I14=Can1.create_image(325,225,image=BLOCK14)

Brique15=Can1.create_rectangle(350,200,400,250)
C15=0
BLOCK15= PhotoImage(file='image/blockhead.gif')
I15=Can1.create_image(375,225,image=BLOCK15)

Brique16=Can1.create_rectangle(400,200,450,250)
C16=0
BLOCK16= PhotoImage(file='image/blockhead.gif')
I16=Can1.create_image(425,225,image=BLOCK16)

Brique17=Can1.create_rectangle(450,200,500,250)
C17=0
BLOCK17= PhotoImage(file='image/blockhead.gif')
I17=Can1.create_image(475,225,image=BLOCK17)

instructions= PhotoImage(file='image/instructions.gif')
cible=Can1.create_image(275,250,image=instructions)

#PAUSE
PAUSE= 1 #PAUSE ON/OFF
imagepause= PhotoImage(file='image/pause.gif')
P=3
PAUPER=1
REPAUSE=1
Perdu=0

#Plein ecran
Pleine= 1


#VIES
Imagevie11= PhotoImage(file='image/vie.gif')
Imagevie1=Can2.create_image(50,100,image=Imagevie11)
Imagevie22= PhotoImage(file='image/vie.gif')
Imagevie2=Can2.create_image(100,100,image=Imagevie22)
Imagevie33= PhotoImage(file='image/vie.gif')
Imagevie3=Can2.create_image(150,100,image=Imagevie33)

VIE1=1
VIE2=1
VIE3=1

nbrvie=3
Gameover1=0

#SCORE

score=0
Scoretext = Can2.create_text(100,400, text="SCORE:"+str(score),font=("Fixedsys Normal",24),fill='white')
high=0
highscoretext= Can2.create_text(100,300, text="Highscore:"+str(high),font=("Fixedsys Normal",20),fill='white')

th_1 = th.Thread(None, countdown, None)
th_2 = th.Thread(None, affichage, None)
timer=0
nul=0
count=1


Can1.bind("<Return>",start)
Can1.bind("<Escape>",quitter)
Can1.bind("<f>",pleinecran)
Can1.bind("<F>",pleinecran)
Can1.bind("<P>",pause)
Can1.bind("<p>",pause)

fenetre.mainloop()
NoSound= PlaySound(None, SND_PURGE)


