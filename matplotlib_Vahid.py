import matplotlib.pyplot as plt

'''
new line in the new branch added branches
you will enjoy this code
matplotlib.org
'''

import numpy as np 

x=np.linspace(0,5,15)
y=x ** 3
print (x,y)

######<<<<<<   functional method

# #Simple drawing
# plt. plot( x, y)
# plt.xlabel('X label')
# plt.ylabel('Y label')
# plt.title('Title')
# plt.show()


# # multi drawing drawing
# plt. subplot( 1, 2, 1)  # (number of rows, number of columns, number of plot you refer to)
# plt.plot(x,y)
# plt. subplot( 1, 2, 2) 
# plt.plot(y,x)
# plt.show()







######<<<<<<   Object Orient method
# ## simple plotting
# fig= plt. figure ()
# axes= fig.add_axes([0.1, 0.1, 0.8, 0.8]) #([left, botton, width, hight]) 
# axes.plot(x,y)
# axes.set_xlabel('X_label')
# axes.set_ylabel('Y_label') 
# axes.set_title('Title')
# plt.show()


# ## double plotting
# fig= plt. figure ()
# axes1= fig.add_axes([0.1, 0.1, 0.8, 0.9])   
# axes1.plot(x,y)

# axes2= fig.add_axes([0.2, 0.5, 0.4, 0.4])   
# axes2.plot(x,y)
# plt.show()







