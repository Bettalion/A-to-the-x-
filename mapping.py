#imports
# import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D 
import numpy as np


def main():

  # Constants Declaration
  Base = -4 # Base^x
  n = 15 #range of x
  density = 100 # intervals
  PrintData = 0# True # 1 or 0
  StoreData = 1
  TITLE = f'Mapping Im & Re : for {Base}^x, x_domain {n}, density {density}'

  x,y,z = genData(Base,n,density)       ## use either of these 
  # x,y,z = read(TITLE)                 ## use either of these 
  if PrintData: print('x:',x,'\n\ny:',y,'\n\nz:',z)
  if StoreData: store(x,y,z,TITLE)
  plot(x,y,z,TITLE)

def genData(Base,n,density): #calculates and creates arrays
  x = np.array(list(map(lambda x: x/density,range(n*density))),dtype=complex) # ,dtype=complex means that the array understands it is a complex number and not Nan
  y = np.array(list(map(
    lambda y: (Base**y).real,x     
      )))
  z = np.array(list(map(
    lambda z: (Base**z).imag,x       
      )))
  return x,y,z

def store(x,y,z,TITLE): #stores current arrays
 np.savetxt(f"x_{TITLE}.csv", x, delimiter=",")
 np.savetxt(f"y_{TITLE}.csv", y, delimiter=",")
 np.savetxt(f"z_{TITLE}.csv", z, delimiter=",")


def read(TITLE): #reads data
  values =[]
  labels=['x','y','z']
  for label in labels:
    f = open(f'{label}_{TITLE}.csv','r')
    data = np.array([complex(x.strip()).real for x in f.readlines()])
    f.close()
    values.append(data)
  return values # x,y,z


def plot(x,y,z,TITLE):  # plots figure
  plt.rcParams['figure.figsize']=(15,10)
  fig = plt.figure(TITLE)
  ax = Axes3D(fig)

  ax.scatter3D(x,z,y)
  ax.set_xlabel('x')
  ax.set_zlabel('y (Re) ')  # better orientation for visualisation
  ax.set_ylabel('z (Im)') # better orientation for visualisation


print('start')
if __name__ == '__main__' :
  main()
  
