# -*- coding: utf-8 -*-
"""
Created on Thu May 27 17:31:51 2021

@author: Eduardo
"""
from claseManejaHelado import ManejaHelado
from claseManejaSabores import ManejaSabores


if __name__ == '__main__':
    mh = ManejaHelado()
    ms = ManejaSabores()
    ms.CargaSabores()
    op = 1 # Variable para seleccionar opcion de menu
    print('Menu')
    while op != 0:        
        print('1- Registrar un helado vendido (Consigna 1).\n2- Mostrar 5 sabores mas pedidos (Consigna 2).\n3- Estimar total de gramos vendido en un sabor (Consigna 3).\n4- Mostrar sabores vendidos segun tipo de helado (Consigna 4).\n0- Salir.')
        print('Opcion adicional \n5- Mostrar lista de todos los helados vendidos.')
        op = int(input('Seleccione opcion:'))
        if op == 1:
            aux = 1
            while aux != 0:
                ms.MuestraSabores()
                sabores = ms.SeleccionSabores()
                mh.RegistraHelado(sabores)
                print('¿Vender otro helado? \n1- Si.\n0- No (terminar).')
                aux = int(input('Opcion:'))
        elif op == 2:
            mh.SaboresMasVendidos()   
        elif op == 3:
            ms.MuestraSabores()
            num = int(input('Ingrese numero de sabor:'))
            mh.GramosVendidoSabor(num)
        elif op == 4:
            tipo = int(input('Ingrese tipo de helado (solo numero):'))
            mh.MuestraSaboresVendidosTamanho(tipo)
        elif op == 5:
            mh.MuestraHeladosVendidos()
        elif op == 0:
            print('Saliendo del programa.')