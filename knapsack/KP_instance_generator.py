import random
import sys

def KPInstanceGenerator(instance_size):
    values = [random.randint(1, 20) for value in xrange(instance_size)]
    weights = [random.randint(1, 20) for value in xrange(instance_size)]
    
    # max_weight = random.randint(10, 15)
    max_weight = random.randint(4*instance_size, 6*instance_size)
    return [max_weight, weights, values]

def writefile(n, W, w, a):
    instance = open('kp_'+str(n)+'_1.dat', 'w')
    instance.write(str(n) + ' ' + str(W) + '\n')
    instance.write(' '.join(map(str, w))+'\n')
    instance.write(' '.join(map(str, a)) )

n = int(sys.argv[1])

values = KPInstanceGenerator(n)
writefile(n, values[0], values[1], values[2])
