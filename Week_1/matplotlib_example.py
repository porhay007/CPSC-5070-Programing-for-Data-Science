from IPython.display import Image

import matplotlib as mpl 
import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace(0,10,100)

#save current style
fig = plt.figure()

plt.plot(x, np.sin(x), '*')
plt.plot(x, np.cos(x), '+')


#plt.show()
#fig.savefig('my_figure.png')

#Image('my_figure.png')


fig.canvas.get_supported_filetypes()

plt.figure()  # create a plot figure

# create the first of two panels and set current axis
plt.subplot(2, 1, 1) # (rows, columns, panel number)
plt.plot(x, np.sin(x))

# create the second panel and set current axis
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))

plt.show()