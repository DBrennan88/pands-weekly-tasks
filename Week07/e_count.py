# Week 7 Task
##Program that reads in a text file and outputs the number of e's it contains. 
## Author Darragh Brennan

#Enter text. programme needs to scan text and count number of Es. then print final count
 # How can i import a text doc?
    # code needed to read test end to end
        #code needed to count Es in text
            #how can i show result of the count


# whats does this mean  = The program should take the filename from an argument on the command line
 # do i specifty file path = # do i specift filename #where will it be saved,  how will my progirrame pull the contents on the file
  # write program. speficy file name in command line to execute programme

import sys # - so i can use text file name in command line argument and pass it to my programme im not sure if im doing this or understanding the terminology right? 

def count_E(LOTR_TEXT): # code to pull doc,  read it,  count e's,  return count
    try:    # file handling statement to use files and set modes.  r used as read only mode here,  filename specified in  function - to be called when running programme
         # getting error- try statements must have and except or finally cluase 
        with open (LOTR_TEXT, 'r') as file: # file variable assigned to my doc here
            text = file.read() # set code to reade file as string of text
            count = text.count("e") + text.count("E") #use the count method for both cases
            return count

    except FileNotFoundError: # add except clause in line with try above - receiving erros previously
        print("Error: File not found.") # formatting errors here as they were not "in line" in the correct sequence
        return -1 #added as part of exception handling when aprevious attmepts generate a black termainl allowing me to type in -  no error message # no realise file was found but prograame below incomplete somewhow
          
# code to pull doc,  read it,  count e's,  return count.  next steps?
# how to exucute here, 
def main():
                            #LOTR_TEXT = input # assigning my doc as the input variable in programme - this seems to be causing me errors
                            #final_count = count_E(LOTR_TEXT) # Set output parameters,  to execute count E function on my text doc
                            # print (final_count) # print the count - not working -  getting syntax error  def main(): SyntaxError: expected 'except' or 'finally' block  - nothing executing here just getging blank terminal no error
                            # none of this worked i need to properly extract file from arugemnt using the "sys"
                                           
   # if final_count != -1: 
   #     print(final_count) # getting same error nothing executing here just getging blank terminal no error would expect a -1?? IndentationError: expected an indented block after function definition on line 32
    try:
        # print("Command-line arguments:", sys.argv)   #used to print argmuents brunninng intp the programme  - Command-line arguments: ['c:\\Users\\darra\\OneDrive\\Desktop\\pands\\pands-weekly-tasks\\Week07\\textdoc.py']
        LOTR_TEXT = sys.argv[1]  # pull file from command line when running programme. treats my text file as a list
         # print("Filename:", LOTR_TEXT)
        final_count = count_E(LOTR_TEXT)
        if final_count != -1:
         print(final_count)
    except IndexError:
        print("Error: File not found.") #still getting this error - it is looking to wrong file in directory! PS C:\Users\darra\OneDrive\Desktop\pands\pands-weekly-tasks\Week06>
        # opend week 7 folder in VS - not getting error so file is found.  but not generated an output 
    

main() # run main prograame #main was indented - getting error again. doc was saved as STY file - changed to text file still not being found in my directory









#REFERENCE  
 # https://www.w3schools.com/python/python_file_handling.asp