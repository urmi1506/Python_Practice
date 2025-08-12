from prettytable import PrettyTable

class Product:
    total_products=[]
    
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    @classmethod
    def addProduct(cls,name,price,quantity):
        new_product={
            'name':name,
            'price':price,
            'quantity':quantity
        }
        cls.total_products.append(new_product)
    @classmethod
    def view_inventory(cls):
         t=PrettyTable(['Products','Price','Stock'])
         for items in cls.total_products:
             t.add_row([items['name'],items['price'],items['quantity']])
         print(t)

    @classmethod
    def sell_products(cls,name,quantity):
        for items in cls.total_products:
            if items['name'] == name:
                if(items['quantity']>=quantity):
                    total_price=items['price']*quantity
                    items['quantity']-=quantity
                    print(f"The sell of {quantity}kg {name} with total price {total_price}")
                    return
                else:
                    print("not enough quantity")
                    return
                
    
    @classmethod
    def view_total_product_count(cls):
        total_cnt=0
        for items in cls.total_products:
            total_cnt +=items['quantity']
            print(f"Total available Product : {total_cnt}")
            

Product.addProduct('Apple',120,2)
Product.addProduct('Strawberry',170,5)
Product.addProduct('Blueberries',250,6)

Product.view_inventory()


Product.sell_products('Strawberry',3)


Product.view_total_product_count()


    