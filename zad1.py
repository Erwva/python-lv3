import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import true


mpg, cyl, hp, wt = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,4,6),delimiter=",", skiprows=1, unpack=true)
a=0
min = 500
srednja = 0
max = 0

for x in data:
    print(data[0:4:3])

sizes = np.random.uniform(10,100,len(mpg))
colors = np.random.uniform(10,100,len(mpg))
for x in cyl:
    a=a+1
    if(x==6):
        if(min > x):
            min=mpg[a]
        if(max < x):
            max=mpg[a]
            srednja = srednja + mpg[a]
    print(min)
    print(max)
    print(srednja/a)
    
   
ax = plt.subplot()
print(wt)
ax.scatter(mpg,hp, s=wt*10, c=colors, vmin=0,vmax=100)
plt.show()
