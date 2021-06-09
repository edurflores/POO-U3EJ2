# -*- coding: utf-8 -*-
"""
Created on Thu May 27 17:35:36 2021

@author: Eduardo
"""

class Helado:
    __gramos = 0
    __sabor = [] # Lista de sabores, puede tener 1 hasta 4
    def __init__(self,gram,sabores):
        self.__gramos = gram
        self.__sabor = sabores
    def GetGramos(self):
        return self.__gramos
    def GetSabores(self):
        return self.__sabor
    def AgregaSabor(self,unSabor):
        self.__sabor.append(unSabor)