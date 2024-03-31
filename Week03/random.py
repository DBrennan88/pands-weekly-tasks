#Week03
#Programme to print out random number
#Author Darragh Brennan

LottoNumber = int 

import random #import existing module

    ###took forever to realise i had not defined the variable
   ###### LottoNumber = random.rand(1, 10) ~~ success
   #######print(LottoNumber) ~~ success

##adding defined list

NewList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

LottoNumber = random.choice(NewList)
print ("And the winning number is: ",  LottoNumber) #~Success



