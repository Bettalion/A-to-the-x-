import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D 
import numpy as np

Base = -2
n = 15 #range of x
density = 100 # intervals
PrintData = 0# True # 1 or 0

TITLE = f'Mapping Im & Re : for {Base}^x, x_domain {n}, density {density}'

def genData(Base,n,density):
  x = np.array(list(map(lambda x: x/density,range(n*density))),dtype=complex) # ,dtype=complex means that the array understands it is a complex number and not Nan
  y = np.array(list(map(
    lambda y: (Base**y).real,x     
      )))
  z = np.array(list(map(
    lambda z: (Base**z).imag,x       
      )))
  return x,y,z

def store(x,y,z):
 np.savetxt(f"x_{TITLE}.csv", x, delimiter=",")
 np.savetxt(f"y_{TITLE}.csv", y, delimiter=",")
 np.savetxt(f"z_{TITLE}.csv", z, delimiter=",")
store(x,y,z)

def read():
  values =[]
  labels=['x','y','z']
  for label in labels:
    f = open(f'{label}_{TITLE}.csv','r')
    data = np.array([complex(x.strip()).real for x in f.readlines()])
    f.close()
    values.append(data)
  return values # x,y,z


  
if PrintData: print('x:',x,'\n\ny:',y,'\n\nz:',z)

def plot(x,y,z):
  plt.rcParams['figure.figsize']=(15,10)
  fig = plt.figure(TITLE)
  ax = Axes3D(fig)

  ax.scatter3D(x,z,y)
  ax.set_xlabel('x')
  ax.set_zlabel('y (Re) ')  # better orientation for visualisation
  ax.set_ylabel('z (Im)') # better orientation for visualisation

  plt.show()

# plot(x,y,z)



x2,y2,z2 = read()
