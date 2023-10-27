
listNames =[] #emply list to store the names 

# store a name to list 

def storeName(name):
    name = name.strip().title()
    if name in listNames:
        return False
    else:
        listNames.append(name)
        return True


# list all names

def printNames():
    print("-"*30)
    for name in listNames:
        print(name)
    print("-"*30)  


# function to search for a name   
def searchName(name):
    name = name.strip().title()
    flag = False
    for item in listNames:
        if name == item:
            flag = True
            break   
    if flag == True: 
        print("name exist in the list")
    else:
        print("name does not Exist") 

while  True:

    print("Menu options")
    print("*"*30)
    print("1, Enter a Name")
    print("2,search a Name")
    print("3,list all Name")
    print("4,Exit")

    choice =int(input("Enter your choice :"))
  
    if choice == 1:
        userinp = input("enter a name ")
        retVal =storeName(userinp)
        if retVal == True:
            print("name added successfully")
        else:
            print("name exists in the list")

    elif choice == 2:
        userinp = input("Enter the name to be searched")
        searchName(userinp)
    elif choice == 3:
        printNames()
    elif choice == 4:
        exit()
    else:
        print("invalid option,please choose correct one!")                  


