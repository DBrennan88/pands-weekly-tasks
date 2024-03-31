#Week03
#Programme to convert floar amount GBP and return absolute amount in GBX
#Author Darragh Brennan


GBPtoConvert= float(-5.99)
     #######     gbxAmout = int  ## added after first attempt to turn output to absolute int
gbxAmout = abs(GBPtoConvert) * 100   

 #####   print (f"{GBPtoConvert} in Pounds is {gbxAmout} in pence") ## output here still as float -5.99 in Pounds is 599.0 in pence

print (f"{GBPtoConvert} in Pounds is {int(gbxAmout)} in pence") ##added int to convert final output from float to int here



