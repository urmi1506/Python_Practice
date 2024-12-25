a=10
if a < 15 :
    print("Hii There..")
else:
    print("Its not satisfied condition")

income=int(input())
if income< 50:
    print("Able to Buy phone")
elif income < 70:
    print("Able to buy car")
elif income < 90:
    print("Able to buy home")
else:
    print("not able to buy anything")

Total_price=int(input())
if Total_price >2000:
    discount= Total_price * .20
    print("discount will be :",discount)
elif Total_price > 5000 :
    discount= Total_price * .50
    print("discount will be :",discount)
else:
    print("No Discount")