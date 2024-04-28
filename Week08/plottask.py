# Week 8 Task
##Program  that that displays a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, and a plot of the function  h(x)=x3 in the range 0 to 10,  on the one set of axes.
## Author Darragh Brennan

##  2 requirements 
    # histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2
    # plot of the function hx(x cubed)  in the range 0 to 10,  on the one set of axes.

'''import pip

import numpy as no # changed interperter to anaconca from VS and solved error -  dont understand how tbh. 


list = [1,2,3,4,5,6]
print (list)'''


#Part 1 creating hisotogram using given criteria
import numpy as np
import matplotlib.pyplot as plt

valuesdistro = np.random.normal(loc=5, scale=2, size=1000)  # data = np.random.normal ~~  generates  random numbers from a normal distribution using nunpys  random normal function. 
#TypeError: normal() got an unexpected keyword argument 'mean' - changed valie to loc.  error using "std" changed to scale
# numpy module to generate randam valies up to 1000,  specifying mean value,  randos will be created to support this mean value. 
#std is telling prgramme the number created using mean of 5 must be withing 2 stds of the mean,  setting parameters for the size of distribution
    
plt.hist(valuesdistro, bins=20) # creates histogram chart by calling matplotlib.pyplot  function. calls variable valuesdistro - bins used to set number of bars
plt.xlabel("X Axis = Values")
        #plt.show() # run succesfully - needed to remove this after part 2 was trouble shooting not realising i was creating 2 graphs not 1 
plt.ylabel("Y Axis = hx")
plt.title('Week08 - plotting data sets on histogram')


#Part 2 plot of the function  h(x)=x3 in the range 0 to 10,  on the one set of axes. compare data sets distribution

x = np.linspace(0, 10, 20) # linespace function here generates 50 numbers between0 and 10 - function evenly spaces nmbers over the specific intervals. plot points dont seem to matter here wont impact output
y = x ** 3  # cubing this x function - range of x is 0 to 10. 0 cubed returns 0.  10 cubed returns 1000 range on the y axis is 0 to 1000
plt.plot(x, y,) # plt.plt starts plotting calling matplotlib.pyplot plot function.


plt.show()



##references 
#course material
##  https://realpython.com/python-histograms/
# datacamp 
# w3 schools https://www.w3schools.com/python/matplotlib_histograms.asp
