# -*- coding: utf-8 --*

"""
    Heurística basada en pesos 
    Autor: Pablo Otniel Aguilar Izaguirre
    Matrícula: 1475648
"""

from knapsack import *

class WeightBasedHeuristic(Knapsack):
    def __init__(self, total_items, max_weight, values, weights):
        Knapsack.__init__(self, total_items, max_weight, values, weights)
    
    def compute_optimal(self):
        if self.all_fit_in_knapsack():
            self.fill_with_all()
        else:
            start = time.time()
            items = self.sort_by_weight()
            current_weight = 0
            for item in items:
                current_weight += item[0]
                if current_weight <= self.max_weight:
                    weight = item[0]
                    value = item[1]
                    print (weight, value)
                    self.optimal += value
                else:
                    current_weight -= item[0]
            
            self.last_weight = current_weight
            self.time = time.time() - start
            self.bytes = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
