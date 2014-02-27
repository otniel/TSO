# -*- coding: utf-8 -*-
"""
    Algorítmo de fuerza bruta para resolver el problema de la mochila
    Autor: Pablo Otniel Aguilar Izaguirre
    Matrícula: 1475648
"""

from knapsack import *

class BrutalKnapsack(Knapsack):
    # Se hereda el constructor de la clase padre
    def __init__(self, total_items, max_weight, values, weights):
        Knapsack.__init__(self, total_items, max_weight, values, weights)
        
    # Convertir de Decimal a Binario
    def decToBin(self, dec, zeros=0):
        return bin(dec).split('b')[1].zfill(zeros)

    # Override por fuerza bruta
    def compute_optimal(self):
        if self.all_fit_in_knapsack():
            self.fill_with_all()
        else:
            start = time.time()
            for x in xrange(2**self.total_items):
                # Iteración en binario
                bits = [int(bit) for bit in self.decToBin(x, self.total_items)]
                # Suma producto de los pesos con la combinación x
                weight = sum([weight*bits[index] for index,weight in enumerate(self.weights)])
                if weight <= self.max_weight:
                    # Suma producto de los valores
                    value = sum([value*bits[index] for index,value in enumerate(self.values)])
                    # Agrega a la lista de factibles
                    self.feasibles.append((weight, value))
                    # Se agrega si es mayor al óptimo anterior
                    if value > self.optimal:
                        self.optimal = value
                        # óptimos locales
                        self.optimals.append((weight, value))
            for optimal in self.optimals:
                print optimal
            # Tiempo
            self.time = time.time() - start
            # Memoria 
            self.bytes = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    
    # Override para imprimir las soluciones óptimas y factibles
    def print_results(self):
        print 'Calculando...'
        self.compute_optimal()
        
        print 'Solución óptima = ', self.optimal
        print 'Total de soluciones factibles = ', len(self.get_feasibles())
        print 'Total de soluciones optimas = ', len(self.global_optimals())
        print 'Tiempo: ', self.get_time(), 'segundos'
        print 'Memoria: ', self.get_bytes(), 'bytes'
