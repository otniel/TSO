
__author__          = "Pablo Otniel Aguilar-Izaguirre" 
__date__            = "Feb 26, 2014" 
__registration__    = "1475648" 
__institution__     = "UANL - FIME"
__email__           = "otnieel.aguilar@gmail.com" 
__license__         = "GNU General Public License"
__version__         = "3 (GPL-3.0)" 
__copyright__       = "Copyright (C) 2014"

"""
    Weight Based Heuristic
"""

from knapsack import *

class WeightBasedHeuristic(Knapsack):
    def __init__(self, total_items, max_weight, values, weights):
        Knapsack.__init__(self, total_items, max_weight, values, weights)
    
    def compute_aproximated(self):
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
                    # DEBUGGIN'
                    # print (weight, value)
                    self.optimal += value
                else:
                    current_weight -= item[0]
            
            self.last_weight = current_weight
            self.time = time.time() - start
            self.bytes = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
