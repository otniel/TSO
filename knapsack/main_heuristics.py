# -*- coding: utf-8 -*-
import sys
import re

from brutal_knapsack import BrutalKnapsack
from vbh import ValueBasedHeuristic
from wbh import WeightBasedHeuristic
from qbh import QuotientBasedHeuristic

def readInstance(file_name):
    # Se crea la instancia (lista con las lineas del archivo)
    instance = [item.rstrip('\n') for item in list(open(file_name))]
    instance = instance[:3]
    instance = [item.split() for item in instance]
    
    for item in instance:
        print item

    # Validación de contenido del archivo
    for line in instance:
        for char in line:
            if re.match('[^\p{L}\d\s_]', char):
                print 'El archivo solo debe contener números, no caracteres especiales'
                exit()
            if char.isalpha():
                print 'El archivo solo debe contener números, no letras'
                exit()
            if re.match('^\d+?\.\d+?$', char):
                print 'El archivo solo debe contener números enteros'
                exit()
            if int(char) < 0:
                print 'El archivo solo debe contener números positivos'
                exit()
            
    return instance

if len(sys.argv) != 2:
    print 'Uso: python brutal_knapsack.py ARCHIVO_INSTANCIA'
    exit()

def main(file_name):
    instance = readInstance(file_name)
        
    # Let the hacking begin!
    n = int(instance[0][0])
    W = instance[0][1]
    w = [item for item in instance[1]]
    a = [item for item in instance[2]]

    print 'Brutal'
    knapsack = BrutalKnapsack(n, W, a, w)
    knapsack.print_results()
    print '\n\n'
   
    print 'Basado en valores'
    knapsack = ValueBasedHeuristic(n, W, a, w)
    knapsack.print_results()
    print '\n\n'
        
    print 'Basado en pesos'
    knapsack = WeightBasedHeuristic(n, W, a, w)
    knapsack.print_results()
    print '\n\n'

    print 'Basado en coeficientes'
    knapsack = QuotientBasedHeuristic(n, W, a, w)
    knapsack.print_results()
    print '\n\n'

main(sys.argv[1])
