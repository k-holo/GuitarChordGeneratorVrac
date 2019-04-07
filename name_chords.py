#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 14:54:37 2019

@author: david
modified by cyril on Sun Apr 7 15:27 2019
"""


# Chromatic Scale
CH_SCALE = {
        "fr" : ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"],
        "en" : ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"],
        "id" : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], # Sur gamme chromatique de Do
        }


def get_scale_from_tonic(tonique, gamme) :
    """ Renvoie une gamme chromatique partant de "tonique" """
    
    ind = CH_SCALE[gamme].index(tonique)
    new_scale = CH_SCALE[gamme][ind:] + CH_SCALE[gamme][:ind]            
    
    return new_scale    


def sort_chord_on_chromatic_scale(chord, gamme):
    """ Trie la liste de notes (chord) sur la gamme chromatique de Do """ 
    
    # retirer les doublons
    chord = set(chord)    
    # echelle chromatique de Do ou C ;°)
    scale = CH_SCALE[gamme]
    # position des notes de l'accord sur l'echelle chromatique
    indices = [scale.index(note) for note in chord]
    # tri de l'acccord en fonction des indices obtenus
    sorted_chord = [note for ind, note in sorted(zip(indices,chord))]
    
    return sorted_chord


def gen_all_chord(sorted_chord):
    """ Renvoie les accords possibles (gen_chords) en prenant une à une les notes de la liste (sorted_chord) comme tonique """

    gen_chords = []
    for i in range(len(sorted_chord)) :
        gen_chords.append( sorted_chord[i:] + sorted_chord[:i] )

    return gen_chords


def get_chord_ind(gen_chord, gamme):
    """ renvoie l'indice des notes de l'accords sur l'echelle chromatique partant de la tonique chord[0] """

    scale = get_scale_from_tonic(gen_chord[0], gamme)
    chord_ind = [scale.index(note)+1 for note in gen_chord]

    return chord_ind


def find_chord_name(chord_ind) :
    """ Cherche les indices/intervalles correspondant dans la liste table_accords_jazzy.txt """

    table = table_accords()
    # accord_name = "inconnu" # j'ai bien compris que c'était juste pour les tests ;°)
    accord_name = None

    for i in range(len(table)):
        if table[i][2] == chord_ind:
            # accord_name = table[i][1][0] # version texte plein
            accord_name = table[i][1][1] # version guitaristique !
            break

    return accord_name


def table_accords():
    """ ouvre et parse le fichiers des accords """
    accords = []
    # f_csv = "table_accords.txt"
    f_csv = "table_accords_jazzy.txt"
    """ separateurs """
    sep = ['\n', "|", ","]

    # def importer_csv(self, f_csv):
    with open(f_csv,'r') as f:
        donnees = f.read()
        donnees_sans_entete = donnees.split(sep[0])
        entete = donnees_sans_entete.pop(0)
        for ligne in donnees_sans_entete:
            if len(ligne) == 0 or ligne[0] == "#":
                continue
            champs = ligne.split(sep[1])
            # famille|noms|harmonie|
            famille = champs[0].strip(" ")
            noms = [x.strip(" ") for x in champs[1].split(sep[2])]
            harmonie = [int(x.strip(" ")) for x in champs[2].split(sep[2])]

            accords.append([famille, noms, harmonie])
    return accords


if __name__ == "__main__" :
    # exemple :
    def fonction_de_demo(liste_de_notes, gamme):
        print(50*"=") # ;°) !!!
        print("accord de départ : " + str(liste_de_notes))
        
        sorted_chord = sort_chord_on_chromatic_scale(liste_de_notes, gamme)
        print("trié : " + str(sorted_chord))
        
        possible = gen_all_chord(sorted_chord)
        print("possibilité : " + str(possible))

        print(25*"=") # ;°) !!!
        # for chord in possible:
            # print("chord tested = " + str(chord))
            
            # chord_ind = get_chord_ind(chord, gamme)
            # print("indice = " + str(chord_ind))
            
            # name = find_chord_name(chord_ind)
            # print(chord[0], name)
            # print(" ")

        ## soit :
        for chord in possible:
            chord_ind = get_chord_ind(chord, gamme)
            name = find_chord_name(chord_ind)

            if name != None:
                print("chord tested = " + str(chord))
                print("indice = " + str(chord_ind))
                print(chord[0] + name)
                print(" ")

    une_liste_de_notes = ["Mi", "Do", "Sol"]
    fonction_de_demo(une_liste_de_notes, 'fr')

    ## depuis un manche de guitare avec les notes numérotées sur les numéros de gamme
    # notes = ["C# 5", "A 4", "E 4", "E 5", "A 3", "E 3"]
    # notes = ["E 3", "C 4", "E 4", "G 4", "C 5", "E 5"]
    # notes = ["E 3", "B 3", "F 4", "A 4", "D 5", "E 5"]

    # notes = ["B 3", "F 4", "A 4", "D 5"]
    notes = [None, "B 3", "F 4", "A 4", "D 5", None] # même accord !!!

    # une_liste_de_notes = [x[0] for x in notes]
    une_liste_de_notes = [x[0] for x in notes if x != None]
    fonction_de_demo(une_liste_de_notes, 'en')
