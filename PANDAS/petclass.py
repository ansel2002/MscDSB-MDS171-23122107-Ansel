class petstore:

    def __init__(self):
        self.details = [{

            "name":"leo",
            "breed":"pitbull",
            "age":"5 years"


        }]




    def storepet(self,name,breed,age):
        print(self.details)

        self.details.append({
            "name":name,
            "breed":breed,
            "age":age
        })


    def searchpet(self):
        
            a = input("enter the pet you want to search")
            if (a == self.details[i]['name'] ):
                print(self.details["name"]["breed"]["age"])
            else:
             print("cant find the pet you searching!!! try again!!!!")      

    






ayjg = petstore()
ayjg.storepet()  
ayjg.searchpet()       
print(ayjg.details)


            
            
