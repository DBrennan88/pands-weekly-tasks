## Week 6 Task
##Program that takes a positive floating-point number as input and outputs an approximation of its square root.
## Create functiojn called  called <tt>sqrt</tt> that does this.
## Author Darragh Brennan

#number = 2008.2024 **messing around
#x = number / 2
#print (x)  # 1004.1012

#   import math  **messing around
#   result = math.sqrt(2008.2024) 
#   print (result)

#def ttsqrtt (number) 
number = 2008.2024
#print (number, ttsqrtt)

def ttsqrtt(number, precision=0.000001):
    x = number / 10  # Initial guess to bring number close to actial square root before function runs
    while True:  # function runs here  = enters loop using newstons method forumla. 
        new_x = 0.5 * (x + number / x)
        if abs(new_x - x) < precision:  # if function checks the difference between new approximaiton and previous approx is less than than the precision. If it is, then the approximation is close enough to the actual square root, so the function returns new_x.
            return new_x  # if the approximation is not precise enough, the new approximation new_x becomes the current approximation x, and the loop continues to define the approximation.
        x = new_x


def find_sqrt(): # Function main created to compute and output the square root approximation using above formula.
    number = 2008.2024 #  diefine my float
    approx_sqrt = ttsqrtt(number)  # we call the function ttsqrtt to define the square root. 
    print(approx_sqrt) #  print the  approximated square root

find_sqrt() #functions defined but need to call this function to execute the code. 


#References used

#https://stackoverflow.com/questions/10725522/arbitrary-precision-of-square-roots 
#https://stackoverflow.com/questions/8222247/newtons-method-in-python