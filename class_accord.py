#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:05:35 2019

@author: david
"""


# Chromatic Scale
CH_SCALE = {
        "fr" : ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"],
        "en" : ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"],
        "id" : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], # Sur gamme chromatique de Do
        }

class Accord:
    
    def __init__(self):
        
        self._ind = []
        
    @property
    def fr(self):
        return self.get_chord('fr')
    
    @fr.setter
    def fr(self, chord):
        self.set_chord(chord, 'fr')
        
    @property
    def en(self):
        return self.get_chord('en')
    
    @en.setter
    def en(self, chord):
        self.set_chord(chord, 'en')
        
    @property
    def id(self):
        return self.get_chord('id')
    
    @id.setter
    def id(self, chord):
        self.set_chord(chord, 'id')
        
    def get_chord(self, lang):
        chord = [CH_SCALE[lang][x] for x in self._ind] 
        return chord
    
    def set_chord(self, chord, lang):
        
        self._ind = [CH_SCALE[lang].index(note) for note in chord]  
        

if __name__ == "__main__" :
    
    accord = Accord()
    print("accord = Accord()")
    accord.fr = ['Mi', 'Sol', 'Do', 'Si']
    print("accord.fr = ['Mi', 'Sol', 'Do', 'Si']")
    print(" ")
    
    print("accord.fr : " + str(accord.fr))
    print("accord.en : " + str(accord.en))
    print("accord.id : " + str(accord.id))
    print(" ")
    accord.en = ['C','B','G']
    print("accord.en = ['C','B','G']")
    print(" ")
    print("accord.fr : " + str(accord.fr))
    print("accord.en : " + str(accord.en))
    print("accord.id : " + str(accord.id))
    
    
    
    
    
    
    
    
    