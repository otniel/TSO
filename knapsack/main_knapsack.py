
__author__          = "Pablo Otniel Aguilar-Izaguirre" 
__date__            = "Feb 26, 2014" 
__registration__    = "1475648" 
__institution__     = "UANL - FIME"
__email__           = "otnieel.aguilar@gmail.com" 
__license__         = "GNU General Public License"
__version__         = "3 (GPL-3.0)" 
__copyright__       = "Copyright (C) 2014"

"""
    Main script
"""

import sys
import re

from brutal_knapsack import BrutalKnapsack
from vbh import ValueBasedHeuristic
from wbh import WeightBasedHeuristic
from qbh import QuotientBasedHeuristic

def readInstance(file_name):
    # Build the instance based on the lines of a given file
    instance = [item.rstrip('\n') for item in list(open(file_name))]
    instance = instance[:3]
    instance = [item.split() for item in instance]
    
    # DEBUGIN'
    # for item in instance:
    #    print item

    # File content validations
    for line in instance:
        for char in line:
            if re.match('[^\p{L}\d\s_]', char):
                print 'The file must have only numbers, not special characters'
                exit()
            if char.isalpha():
                print 'The file must have only numbers, not letters'
                exit()
            if re.match('^\d+?\.\d+?$', char):
                print 'The file must have only integer numbers'
                exit()
            if int(char) < 0:
                print 'The file must have only positive numbers'
                exit()
            
    return instance

if len(sys.argv) != 2:
    print 'Usage: python main_knapsack.py INSTANCE_FILE'
    exit()

def main(file_name):
    instance = readInstance(file_name)
        
    # Let the hacking begin!
    n = int(instance[0][0])
    W = instance[0][1]
    w = [item for item in instance[1]]
    a = [item for item in instance[2]]

    # DEBUGGIN'
    # print 'Brutal'
    # knapsack = BrutalKnapsack(n, W, a, w)
    # knapsack.print_results()
    # print '\n'
   
    print 'Value Based'
    knapsack = ValueBasedHeuristic(n, W, a, w)
    knapsack.print_results()
    print '\n'
        
    print 'Weight Based'
    knapsack = WeightBasedHeuristic(n, W, a, w)
    knapsack.print_results()
    print '\n'

    print 'Quotient Based'
    knapsack = QuotientBasedHeuristic(n, W, a, w)
    knapsack.print_results()
    print '\n'

main(sys.argv[1])
