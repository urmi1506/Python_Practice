from datetime import date
import json


vehicles=[]
rentals=[]
rental_history=[]

def load_vehicles():
    try:
        with open("vehicles.txt","r")as f:
            for line in f:
                data=json.loads(line)
                # vehicle_id,types,model,status=line.strip().split(',')
                # data={
                #     'vehicle_id':int(vehicle_id),
                #     'type':types,
                #     'model':model,
                #     'status':status
                # }
                vehicles.append(data)
    except FileNotFoundError:
        print("File not found")

def load_rentals():
    try:
        with open("rentals.txt","r")as f:
            for line in f:
                data=json.loads(line)
                rentals.append(data)
    except FileNotFoundError:
        print("File Not Found")

def load_rental_history():
    try:
        with open("rental_history.txt","r")as f:
            for line in f:
                data=json.loads(line)
                rental_history.append(data)
    except FileNotFoundError:
        print("File Not Found")

def load_all_data():
    load_vehicles()
    load_rentals()
    load_rental_history()

def add_vehicle():
    vehicle_id=input("Enter Vehicle id:")
    types=input("Enter Type of vehicles:")
    model=input("Enter Model:")
    status=input("Enter Status:")
    daily_rate=int(input("Enter Daily rate"))
    add={
        'vehicle_id':vehicle_id,
        'type':types,
        'model':model,
        'status':status,
        'daily_rate':daily_rate
    }
    vehicles.append(add)

    with open("vehicles.txt","w")as f:
        for item in vehicles:
            f.write(json.dumps(item)+"\n")

def rent_vehicle():
    name=input("Enter Username:")
    vehicle_id=input("Enter vehicle ID:")
    for x in vehicles:
        if x['status']=="Available"and x['vehicle_id']==vehicle_id:
            rent_date=str(date.today())
            rent_vehicle_data(name,vehicle_id,rent_date)
            x['status']="Rented"
            save_rent_vehicle()
            print("Vehicle rented Successfully")
            return
    print("Vehicle not available")


def rent_vehicle_data(name,vehicle_id,rent_date):
    new_data={
        'name':name,
        'vehicle_id':vehicle_id,
        'rent_date':rent_date
    }
    rentals.append(new_data)

def save_rent_vehicle():
    with open("rentals.txt","w")as f:
        for x in rentals:
            f.write(json.dumps(x)+"\n")

    with open("vehicles.txt","w")as f:
        for v in vehicles:
            f.write(json.dumps(v)+"\n")

def return_vehicle():
    vehicle_id=input("Enter vehicle ID:")
    for rental in rentals[:]:
        if rental['vehicle_id']==vehicle_id and "rent_date" in rental:
            for vehicle in vehicles:
                if vehicle['vehicle_id']==vehicle_id:
                    vehicle['status']="Available"
                    daily_rate=vehicle.get('daily_rate',0)
            return_date=date.today()
            rent_date = date.fromisoformat(rental['rent_date'])
            duration=(return_date-rent_date).days
            cost=duration * daily_rate
            rental['return_date']=str(return_date)
            rental['cost'] =cost
            rentals.remove(rental)
            rental_history.append(rental)
            print(f"Vehicle returned and Total cost:rs{cost}")
            save_return_vehicle()
            break
    else:
        print("No Active rental found of this id")

def save_return_vehicle():
    with open("vehicles.txt","w")as f:
        for v in vehicles:
            f.write(json.dumps(v)+"\n")

    with open("rentals.txt","w")as f:
        for r in rentals:
            f.write(json.dumps(r)+"\n")

    with open("rental_history.txt","w")as f:
        for h in rental_history:
            f.write(json.dumps(h)+"\n")

def view_curr_rental():
    for data in rentals:
        if 'rent_date' in data:
            print(f"Name:{data['name']},Vehicle_ID:{data['vehicle_id']},Rent_Date:{data['rent_date']}")

def view_available_vehicle():
    for data in vehicles:
        if data['status'] == "Available":
            print(f"vehicle_ID:{data['vehicle_id']},type:{data['type']},model:{data['model']},status:{data['status']}")

load_all_data()

while True:
    print("1. Add Available Vehicles")
    print("2. Rent a Vehicle")
    print("3. Return Vehicle")
    print("4. View Current Rentals")
    print("5. View Available Vehicles")
    print("6.Exit")
    
    try:
        ch=int(input("Enter Choice:"))
    except ValueError:
        print("Invalid numeric value entered")

    if ch==1:
        add_vehicle()
    elif ch==2:
        rent_vehicle()
    elif ch==3:
        return_vehicle()
    elif ch==4:
        view_curr_rental()
    elif ch==5:
        view_available_vehicle()
    elif ch==6:
        print("Existing..")
        break
    else:
        print("Invalid choice is entered")
    