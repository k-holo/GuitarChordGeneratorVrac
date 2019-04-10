#!/usr/bin/env python3
# -*- coding: UTF8 -*-
"""
module d'affichage de la grille de guitare en vertical

dépendance 'interne' : frm_choix_premiere_case
"""

import tkinter as tk
from tkinter import Canvas

from frm_choix_premiere_case import GuiChoixPremiereCase


__title__ = "Ki_tare chords"
__author__ = 'Ury Cyril : kholo'
__license__ = 'cc'
__copyright__ = 'Creative Common 2018-2019'
__ver_major__ = 0
__ver_minor__ = 1
__ver_patch__ = 0
__ver_sub__ = ''
__version__ = "%d.%d.%d%s" % (__ver_major__, __ver_minor__,
                              __ver_patch__, __ver_sub__)


class Grille(object):
    """ Grille guitare pour placer des points  """
    def __init__(self, parent, *args, **kwargs):
        """  """
        self.parent = parent
        ### TODO : lier avec guitare
        ## ********************************************
        ## ********************************************
        ## ********************************************
        # self.notes = [(1, "C"), (2, "C#"), (3, "D"), (4, "D#"), 
            # (5, "E"), (6, "F"), (7, "F#"), (8, "G"), (9, "G#"), 
            # (10, "A"), (11, "A#"), (12, "B")]
        self.cordes_a_vide = ["E 3", "A 3", "D 4", "G 4", "B 4", "E 5"]
        t = [42, 32, 24, 16, 11, 9] ## tirants
        """  """
        ## self.couleurs_points = ["white", "yellow", "grey"]
        ## self.couleurs_points = ["grey", "yellow", "red"]
        self.couleurs_points = ["grey", "black", "red"]
        ## ********************************************
        ## ********************************************
        ## ********************************************

        self.largeur = 130       ## TODO : adapter au conteneur
        self.hauteur = 280       ## TODO : adapter au conteneur
        self.nbre_cordes = len(self.cordes_a_vide)

        """ origine en [x, y] de la grille dans le conteneur 
        le conteneur est un canvas 
        #self.configure(width=150) ## info
        #self.configure(height=300) ## info
        """
        origineX = (150 - self.largeur) / 2 + 17 ## TODO : adapter au conteneur
        origineY = (300 - self.hauteur) / 2 + 22 ## TODO : adapter au conteneur
        ## print("origine", str(origineX), str(origineY))
        self.origine = [origineX, origineY]   ## TODO : adapter au conteneur

        """ écrat entre les cordes : fin x - debut x"""
        self.debut = int(self.origine[0] + 0)
        self.fin = int(self.origine[0] + self.largeur)
        ecart = int((self.fin - self.debut) / (self.nbre_cordes))
        """ emplacement de la tête en y """
        Tete = self.origine[1]

        """ liste des x de l'emplacement des cordes """
        ## self.suite = [x for x in range(debut, fin, int(ecart))]
        self.suite = [x for x in range(self.debut, self.fin, ecart)]
        if len(self.suite) > self.nbre_cordes:
            self.suite.pop(len(self.suite)-1)
        ## print(self.suite)
        cordes = []

        ### déporté plus loin pour avoir les cordes au dessus des ronds... mais c'est pas pratique ensuite TODO
        ## for num in range(self.nbre_cordes):
            ## corde = parent.create_line(self.suite[num], Tete, self.suite[num], self.hauteur, fill="black", width=t[num]/10)
            ## cordes.append(corde)

        ### frets
        self.frets = self.calculs_position_y_frets()
        for num_f in self.frets:
            x = self.frets[num_f]
            self.parent.create_line(self.origine[1]-7, x, self.largeur+3, x, fill="black", width=3)

        """### tous les points """
        self.points = {} ## point: [[coord_x, coord_y], [corde, fret]]
        self.pts_haut_manche = {} ## les points en haut du manche peuvent avoir du rouge
        self.afficher_tous_les_points()
        ## print("tous les points", self.points)
        ## p_test = 46
        ## print("un point", p_test, self.points[p_test])

        """ défini le numéro de la première case """
        self.premiere_case = 1
        #self.premiere_case_txt = 
        self.premiere_case_txt = self.parent.create_text(9, 45,
                    font="Ubuntu 12 italic bold", 
                    fill="darkblue", 
                    text=str(self.premiere_case), 
                    tags=("premiere_case"))
        self.parent.tag_bind(self.premiere_case_txt, '<ButtonPress-1>', self.set_premiere_case)

        ## j'affiche les cordes après pour qu'elles soient au dessus
        for num in range(self.nbre_cordes):
            corde = parent.create_line(self.suite[num], Tete, self.suite[num], self.hauteur, fill="black", width=t[num]/10)
            cordes.append(corde)


        ## create_text(100,10,fill="darkblue",font="Times 20 italic bold",
                        ## text="Click the bubbles that are multiples of two.")

        self.mode = "edit" # j'utilise un mode vue pour virer les points qui ne servent à rien
        """ pour enregistrer l'état des points """
        self.zero = []
        self.un = [] 
        self.deux = []
        self.diagramme = []
        """  """

    # def fake_function(self):
        # """ fonction temporaire juste pour les tests """
        # pass        


    def set_premiere_case(self, event):
        """ méthode pour choisir le niveau de la première case (en haut) """
        #gui_c_p_c = GuiChoixPremiereCase(self, 3)
        gui_c_p_c = GuiChoixPremiereCase(self, self.premiere_case)
        self.parent.parent.wait_window(gui_c_p_c)
        self.premiere_case = gui_c_p_c.premiere_case
        self.parent.itemconfigure(self.premiere_case_txt, text=str(self.premiere_case) )
        print("premiere_case", self.premiere_case)

    def calculs_position_y_frets(self):
        """ calcul la position en y des frets """
        frets = {}
        LG = self.hauteur - self.origine[1]
        nbreFrets = 5
        for i in range(0, nbreFrets):
            x = (int(LG / nbreFrets) * (i)) + 3
            frets[i] = (self.debut + x)
        ## print(frets)
        return frets
    def afficher_tous_les_points(self):
        """  """
        les_x = self.suite

        derive = 37 ## TODO 
        a_vide = 30 - 7 ### place des points en haut
        les_y = [a_vide]
        ## les_y = [] ## sans celui à vide
        cf = self.calculs_position_y_frets()
        les_y.extend([cf[x] - a_vide / 2 + derive for x in cf])
        ## t = 7 ### t est rayon des points
        t = 9 ### t est rayon des points
        ## print("les_x", les_x)
        ## print("les_y", les_y)

        corde = 0
        m = 0
        for y in les_y:
            fret = 0
            n = 0
            for x in les_x:
                le_tag = '"' + str(m) + "," + str(n) + '"'
                point = self.parent.create_oval(x-t, y-t, x+t, y+t, 
                    fill=self.couleurs_points[0], 
                    outline='gray25',
                    tags=(le_tag))
                self.points[point] = ([x, y], [corde, fret+1])
                ## if fret == 0:
                if corde == 0:
                    self.pts_haut_manche[point] = ([x, y], [corde, fret+1])
                self.parent.tag_bind(point, '<ButtonPress-1>', self.click_point)
                n += 1
                fret += 1
            m += 1
            corde += 1
    def click_point(self, event):
        """  """
        pass

class MyCanvas(tk.Canvas):
    """ Conteneur pour une grille """
    def __init__(self, parent, *args, **kwargs):
        """  """
        self.parent = parent
        super().__init__(*args, **kwargs)
        self.configure(width=150)
        self.configure(height=300)
        # self.configure(bg='white')
        self.configure(bg='grey')
        self.grille = Grille(self)


class Fenetre(tk.Tk):
    """  """
    def __init__(self, parent, *args, **kwargs):
        """  """
        self.parent = parent
        super().__init__(parent, *args, **kwargs)
        self.title("Fenetre")
        self.geometry("+300+300")
        #********************************************
        self.canvas = MyCanvas(self)
        self.canvas.grid()
        #********************************************
        """ pour fermer la fenetre avec le bouton escape """
        self.bind('<Escape>', lambda event: self.quit())
        """ la boucle de GUI """
        self.mainloop()


if __name__ == "__main__":
    Fenetre(None)
