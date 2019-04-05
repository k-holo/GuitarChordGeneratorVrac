#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 14:54:37 2019

@author: david
"""


# Chromatic Scale
CH_SCALE = {
        "fr" : ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"],
        "en" : ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"],
        "id" : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], # Sur gamme chromatique de Do
        }


def get_scale_from_tonic(tonique) :
    """ Renvoie une gamme chromatique partant de "tonique" """
    
    ind = CH_SCALE['fr'].index(tonique)
    new_scale = CH_SCALE['fr'][ind:] + CH_SCALE['fr'][:ind]            
    
    return new_scale    


def sort_chord_on_chromatic_scale(chord):
    """ Trie la liste de notes (chord) sur la gamme chromatique de Do """ 
    
    # retirer les doublons
    chord = set(chord)    
    # echelle chromatique de Do
    scale = CH_SCALE["fr"]
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


def get_chord_ind(gen_chord):
    """ renvoie l'indice des notes de l'accords sur l'echelle chromatique partant de la tonique chord[0] """
    
    scale = get_scale_from_tonic(gen_chord[0])
    chord_ind = [scale.index(note)+1 for note in gen_chord]
    
    return chord_ind


def find_chord_name(chord_ind) :
    """ Cherche les indices/intervalles correspondant dans la liste table_accords_jazzy.txt """
    
    table = table_accords()
    accord_name = "inconnu"
    
    for i in range(len(table)):
        if table[i][2] == chord_ind:
            accord_name = table[i][1][0]
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
    chord = ["Mi", "Do", "Sol"]
    print("accord de départ : " + str(chord))
    
    sorted_chord = sort_chord_on_chromatic_scale(chord)
    print("trié : " + str(sorted_chord))
    
    possible = gen_all_chord(sorted_chord)
    print("possibilité : " + str(possible))
    
    print("========================================================")
    for chord in possible:
        print("chord tested = " + str(chord))
        
        chord_ind = get_chord_ind(chord)
        print("indice = " + str(chord_ind))
        
        name = find_chord_name(chord_ind)
        print(name)
        print(" ")
    
 