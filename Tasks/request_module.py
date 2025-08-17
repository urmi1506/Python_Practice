import json
import requests

class BookStore:
    total_api_call=0
    base_url="https://jsonplaceholder.typicode.com"
    def __init__ (self ,store_name,base_url,store_api):
        self.store_name=store_name
        self.base_url=base_url
        self.store_api=store_api

    def add_book(self,book_id,title,author,price):
         data={
             'book_id':book_id,
             'title':title,
             'author':author,
             'price':price

         }
         r=requests.post(f"{self.base_url}/posts",json=data)
         BookStore.total_api_call +=1
         details=r.json()
         pretty_json = json.dumps(details, indent=4, sort_keys=True)
         return pretty_json
    
    def get_book(self,book_id):
         r=requests.get(f"{self.base_url}/posts/{book_id}")
         BookStore.total_api_call +=1
         details=r.json()
         pretty_json = json.dumps(details, indent=4, sort_keys=True)
         return pretty_json

    def update_book(self,book_id,new_data):
         r=requests.put(f"{self.base_url}/posts/{book_id}",json=new_data)
         BookStore.total_api_call +=1
         details=r.json()
         pretty_json = json.dumps(details, indent=4, sort_keys=True)
         return pretty_json


    def delete_book(self,book_id):
         r=requests.delete(f"{self.base_url}/posts/{book_id}")
         BookStore.total_api_call +=1
         details=r.json()
         pretty_json = json.dumps(details, indent=4, sort_keys=True)
         return pretty_json

    @classmethod
    def get_total_api_calls(cls):
         return cls.total_api_call
    
def main():
     
     store=BookStore("urmi's BookShop",
                     base_url="https://jsonplaceholder.typicode.com",
                     store_api="xyz123")
     
     print("Add book")
     print(store.add_book(book_id=101,title="python",author="xyz",price=500))

     print("\n Get Book")
     print(store.get_book(book_id=1))

     print("\n Update Book")
     new_data = {"id":1, "title":"Java","author":"xyz","price":600}
     print(store.update_book(book_id=1 ,new_data=new_data))

     print("\n Delete book")
     print(store.delete_book(book_id=1))

     print("Total API call :",BookStore.get_total_api_calls())

if __name__ == "__main__":
     main()