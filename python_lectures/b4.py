lst= input("enter some values")
a = lst.split(";")

even =[]
for i in a:
    if int(i)%2==0:
        even.append(i)
    else:
        exit

even            