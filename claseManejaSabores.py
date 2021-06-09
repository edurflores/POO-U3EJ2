# -*- coding: utf-8 -*-
"""
Created on Thu May 27 17:53:52 2021

@author: Eduardo
"""
import csv
from claseSabor import Sabor

class ManejaSabores:
    def __init__(self):
        self.__listaSabores = []
    def CargaEnLista(self,unSabor):
        self.__listaSabores.append(unSabor)
    def CargaSabores(self):
        archivo = open('sabores.txt')
        reader = csv.reader(archivo, delimiter=',')
        ban = False
        for fila in reader:
            if ban == False: # Saltea primera linea
                ban = True
            else:
                num = int(fila[0])
                nomb = fila[1]
                desc = fila[2]
                unSabor = Sabor(num, nomb, desc)
                self.CargaEnLista(unSabor)
        archivo.close()
        print('Se han cargado los sabores.')
    def MuestraSabores(self):
        print('Listado de sabores.')
        print('--------------------------------')
        print('Numero \t| Nombre \t| Descripcion')
        print('--------------------------------')
        for i in range(len(self.__listaSabores)):
            print('{} \t| {} \t| {}'.format(str(self.__listaSabores[i].GetNumeroSabor()),str(self.__listaSabores[i].GetNombreSabor()),str(self.__listaSabores[i].GetDescripcionSabor())))
            print('--------------------------------')
    def GetListaSabores(self):
        return self.__listaSabores
    def RetornaSabor(self,numsab):
        print('Entra a funcion retorna sabor')
        print('Cantidad de sabores registrados:',len(self.__listaSabores))
        for i in range(len(self.__listaSabores)):
            print('Entra a for')
            if self.__listaSabores[i].GetNumeroSabor() == numsab:
                print('Sabor encontrado:',self.__listaSabores[i].GetNombreSabor())
                print('Descripcion:',self.__listaSabores[i].GetDescripcionSabor())
                return self.__listaSabores[i]
    def SeleccionSabores(self): # Funcion que devuelve una lista de sabores seleccionados para el helado
        cant = 0 # Cantidad de sabores seleccionados
        sabores = [] # Lista en que se guardan sabores seleccionados
        print('Seleccion de sabores')
        print('Seleccione sabores mediante numero de sabor (maxima cantidad 4)')
        numsab = int(input('Numero de sabor:'))
        for i in range(len(self.__listaSabores)):
            if self.__listaSabores[i].GetNumeroSabor() == numsab:
                sabores.append(self.__listaSabores[i])
                cant += 1
                print('Sabor seleccionado.')
                break
        print('¿Agregar otro sabor?\n1- Si.\n0- No (no agrega mas sabores).')
        aux = int(input('Opcion:'))
        while aux != 0 and cant < 4:
            if aux == 1:
                numsab = int(input('Numero de sabor:'))
                for i in range(len(self.__listaSabores)):
                    if self.__listaSabores[i].GetNumeroSabor() == numsab:
                        sabores.append(self.__listaSabores[i])
                        cant += 1
                        print('Sabor seleccionado.')
                        break
                print('¿Agregar otro sabor?\n1- Si.\n0- No (no agrega mas sabores).')
                aux = int(input('Opcion:'))
            else:
                print('Sabores registrados.')
        return sabores