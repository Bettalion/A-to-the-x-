import random
import math
import matplotlib.pyplot as plt
import itertools

BASE = math.e
interval_inc = 100
Range = 1
# def func_y(x):
#  print('going through')
#  return x**2

# x = [1,2,3,4,5,6,7]
x = list(map(lambda x:x/interval_inc,range(Range*interval_inc)))
y = list(map(lambda x:BASE**x,x)) 

print(x,y)

plt.plot(x,y)
plt.show()



print('Done!')