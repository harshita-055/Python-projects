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
  name        
          
  
    
