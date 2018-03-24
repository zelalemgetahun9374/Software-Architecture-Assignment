import sqlite3
# the control class mediates between model and view
class Control:
    def getModelDescription(self, productmodel):
        model = Model()
        view   = View()
        description_data = model.getDescription(productmodel)
        return view.description(description_data, productmodel)
    def getProductList(self, product):
        model = Model()
        view   = View()
        productlist_data = model.getProductList(product)
        return view.productList(productlist_data, product)
# model class contains code for manipulating database
class Model:
    def getProductList(self, product):
        query = "select ID, Brand, Model from products where Brand = '%s' " %product
        productlist = self._dbselect(query)
        list1 = []
        i = 0
        for row in productlist:
            list1.append([row[0],row[1],row[2]])
            i += 1
        return list1
    def getDescription(self, phone_model):
        query = "select Description from products where Model = '%s' " % phone_model
        description = self._dbselect(query)
        for row in description:
            return row[0]
    def _dbselect(self, query):
        connection = sqlite3.connect('shop')
        cursorObj = connection.cursor()
        results = cursorObj.execute(query)
        connection.commit()
        #cursorObj.close()
        return results

# view class contains code for choosing the view to present based on the user input
class View:
    def description(self, description, productmodel):
        print (" Product Description for " + productmodel )
        print(str(description))
    def productList(self, list1, product):
        print (" Product List for "+ product + "\n")
        print(" Id  Brand Model")
        for product in list1:
            print (" " + str(product[0]) + "   " + str(product[1]) + "  " + str(product[2]))
    def menu(self):
        print (" Welcome to Ethio-phones shop info app")
        print ("     Enter your choice")
        print(" 1. view product list of a phone company")
        print(" 2. get a descirption of phone model \n")
        choice = eval(input())
        while(choice != 1 and choice != 2):
            print("Enter valid choice.\n")
            print("     Enter your choice")
            print(" 1. view product list of a phone company")
            choice = eval(input(" 2. get a descirption of phone model \n"))
        
        controller = Control()
        if (choice == 1):
            brand = input(" Enter the brand name").lower()
            controller.getProductList(brand)
        else: 
            phone_model = input(" Enter the model's name")
            controller.getModelDescription(phone_model)
 

view = View()
view.menu()                    
