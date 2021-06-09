# -*- coding: utf-8 -*-
"""
Created on Thu May 27 17:36:32 2021

@author: Eduardo
"""

class Sabor:
    __numero = 0
    __nombre = ''
    __descripcion = ''
    def __init__(self,num,nomb,desc):
        self.__numero = num
        self.__nombre = nomb
        self.__descripcion = desc
    def GetNumeroSabor(self):
        return self.__numero
    def GetNombreSabor(self):
        return self.__nombre
    def GetDescripcionSabor(self):
        return self.__descripcion