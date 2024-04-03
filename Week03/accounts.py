##Week 3 Task
##Programme  to read in 10 characters and outputs only last 4 with X replacing initial 6 digits. also to deal with accounts numbers of any length
##Author Darragh Brennan

Darraghs_Account =  str(1234567890)                  ##Assign value (acc no) to string variable Darraghs Account 
Private_view = "X" * 6 + Darraghs_Account[6:]        ##New variable Private_view should pull in Darraghs Ac No,  and replace string X 6 times 
                                                     ## + operstor used to concatenate 6 Xs with Darraghs account number in the string          
                                                                                            

###  print (Darraghs_Account[6:])                     ##New Darraghs_Account[6:]  cuts frist 6 charaters off the variable.  [ used for slicing ]   : slice up to semi colon - so slive first 6 characters here and output from 7 on. 
print (Private_view)

##How to deal with acc's of any length - to always slice string leaving final 4 digits regarless of length - how to a not specify digits to conc/replace ?  do i need t flip the semi colon?

Darraghs_Account1 =  str(123456789123456789)                       #Assign value (acc no) to string variable Darraghs Accounts
Darraghs_Account2 =  str(123456789123456789123456789)  
Darraghs_Account3 =  str(123456789123456789123456789123456789)            

Private_view1 = "X" * (len(Darraghs_Account1) - 4) + Darraghs_Account1[-4:]       # i want to see the length of my string. reduce it by 4. i want the origonal 4 end digits. 
                                                                                  # print (len(Darraghs_Account1) - 4)  = 14 i want to replace these with my X string
                                                                                  # + operater to add my 14*Xs to whats left of my account number 
                                                                                  # print (Darraghs_Account1[-4:])  -again slicing the acc no up to the last 4 - flipping semo colon
Private_view2 = "X" * (len(Darraghs_Account2) - 4) + Darraghs_Account2[-4:] 
                       
Private_view3 = "X" * (len(Darraghs_Account3) - 4) + Darraghs_Account3[-4:] 


print (Private_view1)
print (Private_view2)
print (Private_view3)
