item_list=[]
summary={}
while True:
    print("---Sales Report Analyzer---")
    print("1.Input Sales Data")
    print("2.Total sales per product")
    print("3.Best-selling product (highest quantity sold)")
    print("4.Most profitable product (based on price × quantity)")
    print("5.Total revenue for the day")
    print("6.Sorted product report by sales amount")
    print("7.Exit")

    try:
        ch=int(input("Enter Choice:"))
    except ValueError:
        print("Invalid Choice Enter")

    match(ch):
        case(1):
            item=input("Enter name of item :")
            quantity=int(input("Enter quantity :"))
            price=float(input("Enter Price per unit :"))

            item_list.append({
                'item':item,
                'quantity':quantity,
                'price_per_unit':price
            })

        case(2):
            print("Total Sales per Product :")
            
            for x in item_list:
                name=x['item']
                qty=x['quantity']
                price=x['price_per_unit']
                
                if name not in summary:
                    summary[name]={'total_qty':0,'total_sales':0.0}
                    summary[name]['total_qty'] +=qty
                    summary[name]['total_sales']+=qty*price
                else:
                    summary[name]['total_qty'] +=qty
                    summary[name]['total_sales']+=qty*price

            for product, data in summary.items():
                print(product , data['total_qty'], f"{data['total_sales']:.2f}")

        case(3):
            product=None
            max_qty=0
            for product, data in summary.items():
                if data['total_qty'] > max_qty:
                    max_qty=data['total_qty']
                    best_product=product
            if best_product:
                print(f"Best-Selling product{product} , {max_qty}")

        case(4):
            most_profitable= None
            highest_revenue=0
            for x in item_list:
                name=x['item']
                qty=x['quantity']
                price=x['price_per_unit']

                total_revenue=qty*price

                if(total_revenue > highest_revenue):
                    highest_revenue=total_revenue
                    most_profitable= name
            if most_profitable:
                print(f"Most Profitable Product :{name}({highest_revenue})")
        
        case(5):
            all_revenue=0
            for x in item_list:
                name=x['item']
                qty=x['quantity']
                price=x['price_per_unit']

                total_revenue=qty*price
                all_revenue +=total_revenue
            print(f"Total Revenue : {all_revenue:.2f}")

        case(6):
            sorted_items = sorted(summary.items(), key=lambda x: x[1]['total_sales'], reverse=True)

            print("Products sorted by sales amount:")
            for product, data in sorted_items:
                 print(product, f"{data['total_sales']:.2f}")
        
        case(7):
            print("Existing...Thank You")  
