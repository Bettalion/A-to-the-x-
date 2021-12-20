b = -1
y = complex(b**0.5)
print(y.imag)

# print(list(range(6)))
# n = 10
# lst = []
# for x in range(n*10):
#   lst.append(x/10)

def func(x):
  ans = (-1)**x
  return ans

# # print(lst)
# # x  = list(range(19))
# x = [0,0.1,0.2,0.3]
# print(b**0.11)
# print(x,'\n',list(map(func,x)))
import numpy as np
density = 10
n= 1

# x = np.array(list(map(lambda x: x/density,range(n*density))))
x = np.array([0,0.1,0.2,0.3],dtype=complex)

print(x,'\n',list(map(func,x)))