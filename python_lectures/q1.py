# # # create a sportmart class , where you will have 
# # => inventory /shelf of items 
# # =>orders for the items





# # # create a csv file which will store your inventory details and order 
# details with the help of file handling techniques in python read the files
#  and create a object for trinity store and populate the inventory items and order for
#  the trinity object . to make sure u have added all the itmes in your file ,
#  use a display method to shpw your inventory and order history



class sportmart:



    def __init__(self):
        self.inventory = []
        self.orders=[]

    

    def display_inventory(self):

        f = open("python_lectures/Inventory_management.csv","r")
        print(f.read())
         



    def display_orders(self):
        f = open("python_lectures/order_management.csv","r")
        print(f.read())    
    


    def create_iventory(self,itemname,qty,price):
        self.details ={

                "itemname" = i,
                
                }




i= input("enter the itemname")
q = input("enter qty value")
p = input("enter a price for the item")



a = sportmart()
a.display_orders()       
            
        

        
