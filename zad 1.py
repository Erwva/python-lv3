import pandas as pd
import numpy as np
#zad 1
mtcars = pd.read_csv('mtcars.csv')
print(mtcars.describe())
print(mtcars.sort_values(by =['mpg']))
#zad 2
print("-----------------------------------------------------------------------------")
print(mtcars[mtcars.cyl >= 8].sort_values(by = ['mpg']).head(3))
#zad 3
print("-----------------------------------------------------------------------------")
mtcars_6 = mtcars[mtcars.cyl == 6]
print(mtcars_6['mpg'].mean())
print("-----------------------------------------------------------------------------")
#zad 4
mtcars_4 = mtcars[(mtcars.cyl == 4) & (mtcars.wt > 2) & (mtcars.wt < 2.2)]
print(mtcars_4.mpg.mean())
print("-----------------------------------------------------------------------------")
#zad 5
print(mtcars['am'].tolist().count(1))
print(mtcars['am'].tolist().count(0))
print("-----------------------------------------------------------------------------")
#zad 6
print(mtcars[mtcars.hp > 100].am.tolist().count(1))
#zad 7
print("-----------------------------------------------------------------------------")
print(mtcars.wt * 1000 * 0.45359237)
