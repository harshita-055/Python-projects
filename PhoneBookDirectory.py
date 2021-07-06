import os
#FUNCTION TO ADD A NEW ENTRY i.e. ADD A NEW NAME AND PHONE NUMBER OF A SUBSCRIBER

def Add_Details():
  entry=[]
  name=input("enter the name:")
  ph_no=input("enter the phone number:")
  entry.append(name)
  entry.append(ph_no)
  return entry

#FUNCTION TO SORT THE CONTENTS OF DIRECTORY IN THE ASCENDING ORDER

def bub_sort():
  length=len(dirList)-1
  unsorted=True
  while unsorted:
    unsoretd=False
    for element in range(0,length):
      if dirList[element] > dirList[element+1]:
        temp=dirList[element+1]
        dirList[element+1]=dirList[element]
        dirList[element]=temp
        #print(dirList)
        unsorted =True
        
 #FUNCTION TO SAVE THE NEWLY ADDED SUBSCRIBERS TO THE DIRECTORY

def SaveDataToFile(dirList):
  f=open("Phone_Directory.txt"."w")
  for n in dirList:
    f.write(n[0])
    f.write(" ")
    f.write(n[1])
    f.write('\n')
  f.close()
  
 #FUNCTION TO DISPLAY TO PRINT ALL THE NAMES AND PHONE NUMNERS OF ALL THE SUSCRIBERS

def Display():
  if(os.path.isfile('Phone_Directory.txt')==0):
    print("Sorry you dont have any contacts in your phone address book")
    print("Please create it!!!)
  elif(os.stat('Phone_Directory.txt').st_size==0):
    print("address book is empty")
  else:
    f=open('Phone_Directory.txt','r')
    text=f.read()
    print(text)
    f.close()
          
#FUNCTION TO FIND PHONE NUMBER OF A PARTICULAR SUBSCRIBER

def Search():
  name=input("Enter the name:")
  f=open("Phone_Directory.txt",'r')
  result=[]
  for line in f:
    if name in line:
      found=True
      break
    else:
      found=False
  if(found==True):
    print("The name of person exist in directory:")
    print(line.replace(',',':'))
  else:
    print("The name does not exist in directory")
          
# FUNCTION TO GET SUBSCRIBER FROM THE USER.THE REQUESTED CHOICE IS RETURNED TO THE MAIN PART IF THE PROGRAM TO PERFORM A PARTICULAR TASK.
  
def get_choice():
  print("1)\tAdd new phone number to a list of phone book directory:")no
  print("2)\tSort name in ascending order")
  print("3)\tSave all the phone numbers to file")        
  print("4)\tPrint all phone book directory on the console")
  print("5)\tSearch phone number from phone directory")  
  print("6)\tPlease write 6 to exit from the menu ") 
  ch=input("Please enter the choice")
  return (ch)
          
#MAIN PROGRAM
          
if(os.path.isfile("Phone_Directory.txt")==0):
  print("Sorry you dont have any contacts in your phone book")
  print("Please create it!!!)
  directory=[]
else:
  print("Already your phone book have some numbers")         
  print("you can see it!!!)              
  directory=[]              
  f=open("Phone_Directory.txt","r")              
  for line in f:
         if (line.endwith("\n")):
                 line=line[:-1]
                 directory.append(line.strip().split(","))
f.close()
#directory=[]
c=True
while c:
        ch= get_choice()
        if ch=='1':
          e=Add_Details()
          directory.append(e)
        
        if ch=='2':
          bub_sort(directory)
          print("Contents of phone book sorted successfully")
                
        if ch=='3':
          SaveDataToFile(directory)
          print("Data saved to phone book successfully")
        
        if ch=='4':
          Display()
        
        if ch=='5':
          Search()
        
        if ch=='6':
          print("Thanks a lot for using our application")
          c=False
      
                
                
                
                
                
                
                
                
                
