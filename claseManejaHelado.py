# -*- coding: utf-8 -*-
"""
Created on Thu May 27 17:54:06 2021

@author: Eduardo
"""
from claseHelado import Helado
class ManejaHelado:
    def __init__(self):
        self.__listaHelados = [] # Helados vendidos
    def AgregaHelado(self,unHelado):
        self.__listaHelados.append(unHelado)
    def RegistraHelado(self,sabores): # Consigna 1
        peso = 0
        print('Seleccione peso del helado')
        print('1- 100 gr.\n2- 150 gr.\n3- 250 gr.\n4- 500 gr.\n5- 1000 gr.')
        op = int(input('Opcion:'))
        if op == 1:
            peso = 100
        elif op == 2:
            peso = 150
        elif op == 3:
            peso = 250
        elif op == 4:
            peso = 500
        elif op == 5:
            peso = 1000
        unHelado = Helado(peso,sabores)
        self.AgregaHelado(unHelado)
        print('Se ha registrado la venta del helado')
    def GramosVendidoSabor(self,numsabor): # Consigna 3
        total = 0
        for i in range(len(self.__listaHelados)):
            sabores = self.__listaHelados[i].GetSabores()
            for j in range(len(sabores)):
                if sabores[j].GetNumeroSabor() == numsabor:
                    total += self.__listaHelados[i].GetGramos() / len(sabores)
        print('Total estimado de gramos vendidos:{} gr'.format(int(total)))
    def MuestraSaboresVendidosTamanho(self,numtipo): # Consigna 4
        print('Sabores vendidos en helados de este tamanho:')
        print('--------------------------------')
        print('Numero \t| Nombre \t')
        for i in range(len(self.__listaHelados)):
            if numtipo == self.__listaHelados[i].GetGramos():
                sabores = self.__listaHelados[i].GetSabores()
                for j in range(len(sabores)):
                    print('{} \t| {}'.format(sabores[j].GetNumeroSabor(),sabores[j].GetNombreSabor()))
        print('--------------------------------')
    def MuestraHeladosVendidos(self): # Funcion opcional para ver helados vendidos
        print('Helados vendidos.')
        for i in range(len(self.__listaHelados)):
            sabores = self.__listaHelados[i].GetSabores()
            print('Tipo:{}'.format(int(self.__listaHelados[i].GetGramos())))
            print('Sabores:')
            for j in range(len(sabores)):
                print('{}'.format(str(sabores[j].GetNombreSabor())))
            print('--------------------------------')
    def SaboresMasVendidos(self): # Consigna 2
        listasab = [] # Lista que guarda todos los sabores vendidos
        for i in range(len(self.__listaHelados)):
            sabores = self.__listaHelados[i].GetSabores()
            for j in range(len(sabores)):
                listasab.append(sabores[j].GetNombreSabor())
        mayores = [] # Lista ordenada con los mas vendidos
        aux = []
        for i in range(len(listasab)):
            if aux.count(listasab[i])<1:
                mayores.append((listasab[i],listasab.count(listasab[i]))) # Agrega el objeto y la cantidad de veces que aparece (tupla)
                aux.append(listasab[i])
        mayores.sort(key=lambda x:x[1],reverse=True) # Ordena de mayor a menor
        print('Los 5 sabores mas vendidos')
        print('Nombre \t| Cantidad de ventas')
        print('--------------------------------')
        for i in range(5):
            print('{} \t| {}'.format(str(mayores[i][0]),int(mayores[i][1])))
        print('--------------------------------')