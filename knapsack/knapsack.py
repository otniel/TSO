# -*- coding: utf-8 -*-

"""
    Clase padre de donde se heredan métodos para resolver el problema de la mochila
    Autor: Pablo Otniel Aguilar Izaguirre
    Matrícula: 1475648
"""

import itertools
import time
import resource

class Knapsack(object):
    def __init__(self, total_items, max_weight, values, weights):
        if total_items != len(values) or total_items != len(weights):
            print 'La cantidad de elementos tanto de valores como de pesos deben ser iguales a el total de items'
            quit()
            
        self.total_items = int(total_items)
        self.max_weight = int(max_weight)
        self.values = [int(value) for value in values]
        self.total_value = sum(self.values)
        self.weights = [int(weight) for weight in weights]
        self.total_weight = sum(self.weights)
        self.feasibles = []
        self.optimals = []
        self.optimal = 0
        self.time = 0.0
        self.bytes = 0.0
        self.last_weight = 0

    def all_fit_in_knapsack(self):
        return self.total_weight <= self.max_weight

    
    def fill_with_all(self):
        start = time.time()
        self.feasibles = list(itertools.product(self.weights, self.values))
        self.optimals = [(self.total_weight, self.total_value)]
        print 'La suma de los pesos de todos los objetos no excede la capacidad de la mochila'
        self.optimal = self.total_value
        # Tiempo
        self.time = time.time() - start
        # Memoria 
        self.bytes = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


    def compute_optimal(self):
        pass
    def get_feasibles(self):
        return self.feasibles
    
    def get_optimals(self):
        return self.optimals
    
    def get_time(self):
        return self.time

    def get_bytes(self):
        return self.bytes
    
    def both_values(self):
        return [(self.weights[index], self.values[index]) for index in range(self.total_items)]

    def global_optimals(self):
        global_optimals=[]
        return [global_optimals.append(opt) for opt in self.optimals if opt[1] == self.optimal]

    def sort_by_value(self):
        return sorted(self.both_values(), key=lambda index: index[1], reverse=True)

    def sort_by_weight(self):
        return sorted(self.both_values(), key=lambda index: index[0])

    def sort_by_quotient(self):
        matriz = [[values, float(values[1]) / float(values[0])] for values in self.both_values()]
        return sorted(matriz, key=lambda index: index[1], reverse=True)

    def print_results(self):
        print 'Calculando...'
        self.compute_optimal()
        
        print 'Solución óptima = ', self.optimal
        print 'Último peso = ', self.last_weight
        print 'Tiempo: ', self.get_time(), 'segundos'
        print 'Memoria: ', self.get_bytes(), 'bytes'
        
