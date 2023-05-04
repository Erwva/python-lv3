import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
mtcars = pd.read_csv('mtcars.csv')

mtcars.groupby('cyl').agg({'mpg':'mean'}).mean()
plt.bar(mtcars['cyl'],mtcars['mpg'])
plt.show()

mtcars.boxplot(by = 'cyl', column='wt')
plt.show()

mtcars.boxplot(by = 'am', column='mpg')
plt.show()

mtcars.plot.scatter(x = 'qsec', y = 'hp', c = 'am')
plt.show()
