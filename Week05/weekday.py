## Week 5 Task
##Program that outputs whether or not today is a weekday.
## Author Darragh Brennan


import datetime ##dates not data type in python - import module datetime to work woth dates  (https://www.w3schools.com/python/python_datetime.asp)

Today = datetime.datetime.now().weekday()  # gets current date and time - output shows weekday as int - do i  to convert to string / name of day ? prob not needed here. 
   ##  print (Today) # Mon is 0 Sun is 6   - worked as expected before added boolean
if Today < 5: # 5 is sat so < 5 shows weekdays only
    print ("Yes,  unfortunately today is a weekday :(")  # no need to f string here not including variable in statement
elif Today <=6 :# we know rule above captures weekdays,  less than or equal to 6 catches both 5 and 6 for Sat and Sun
    print ("It is the weekend!!")


