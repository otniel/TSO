
__author__          = "Pablo Otniel Aguilar-Izaguirre" 
__date__            = "Feb 26, 2014" 
__registration__    = "1475648" 
__institution__     = "UANL - FIME"
__email__           = "otnieel.aguilar@gmail.com" 
__license__         = "GNU General Public License"
__version__         = "3 (GPL-3.0)" 
__copyright__       = "Copyright (C) 2014"

"""
    Brutal force algorithm
"""

from knapsack import *

class BrutalKnapsack(Knapsack):
    # Inherit parent class constructor
    def __init__(self, total_items, max_weight, values, weights):
        Knapsack.__init__(self, total_items, max_weight, values, weights)
        
    def decToBin(self, dec, zeros=0):
        return bin(dec).split('b')[1].zfill(zeros)

    # Override 
    def compute_optimal(self):
        if self.all_fit_in_knapsack():
            self.fill_with_all()
        else:
            start = time.time()
            for x in xrange(2**self.total_items):
                bits = [int(bit) for bit in self.decToBin(x, self.total_items)]
                
                weight = sum([weight*bits[index] for index,weight in enumerate(self.weights)])
                if weight <= self.max_weight:
                    value = sum([value*bits[index] for index,value in enumerate(self.values)])
                    self.feasibles.append((weight, value))
                    if value > self.optimal:
                        self.optimal = value
                        self.optimals.append((weight, value))
                        
            self.time = time.time() - start
            self.bytes = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    
    # Override
    def print_results(self):
        print 'Computing...'
        self.compute_optimal()
        
        print 'Optimal Solution\t: ', self.optimal
        # DEBUGGIN'
        # print 'Total feasible solutions = ', len(self.get_feasibles())
        # print 'Total optimal solutions = ', len(self.global_optimals())
        print 'Time\t\t\t: ', self.get_time(), '\t secs'
        print 'Memory\t\t\t: ', self.get_bytes(), '\t\t bytes'
