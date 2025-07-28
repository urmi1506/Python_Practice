import datetime
class Patient:
    def __init__(self, **kwargs):
        self.patient_id=kwargs.get("patient_id")
        self.name=kwargs.get("name")
        self.age=kwargs.get("age")
        self.gender=kwargs.get("gender")
        self.contact=kwargs.get("contact")
        self.symptoms=kwargs.get('symptoms',[])
        self.visit_hist=kwargs.get('visit_hist',{})
    
    def update_info(self,contact=None ,new_symptoms=None):
        if contact :
            self.contact=contact
        if new_symptoms:
            self.symptoms.extend(new_symptoms)
            today_date=datetime.datetime.now().strftime("%Y-%m-%d")
            self.visit_hist[today_date]=new_symptoms

    def display(self):
        print(f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}")
        print(f"Contact: {self.contact}")
        print(f"Symptoms: {self.symptoms}")
        print(f"Visit History: {self.visit_hist}")


patients=[]
def add_patient():
    try:
        patient_id=int(input("Enter patient ID:"))
        age=int(input("Enter Age:"))
        contact=int(input("Enter Contact:"))
    except ValueError:
        print("Invalid data entered.")
        return
    
    name=input("Enter name :")
    gender=input("Enter Gender(M/F/O):")
    symptom=input("Enter Symptoms")
    date_today = datetime.datetime.now().strftime("%Y-%m-%d")

    for p in patients:
        if p.patient_id==patient_id:
          print("Patient Already Present.")
          return
        
    visit_hist={
       date_today:symptom
    }
    patient=Patient(
        patient_id=patient_id,
        name=name,
        age=age,
        gender=gender,
        contact=contact,
        symptoms=[symptom],
        visit_hist=visit_hist
    )
    patients.append(patient)
    print("Patient added Successfully")


def view_patient():
    if not patients:
        print("No patient Available")
        return

    for patient in patients:
        patient.display()
    
def search():
    try:
        patient_id=int(input("Enter Patient ID to search:"))
    except ValueError:
        print("Invalid value entered.")
    for patient in patients:
        if patient.patient_id==patient_id:
            print("Patient found:")
            patient.display()
            return
    print("patient not found.")

def update():
    try:
        patient_id = int(input("Enter Patient ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return

    for patient in patients:
        if patient.patient_id == patient_id:
            new_contact = input("Enter new contact: ")
            if new_contact:
                try:
                    patient.contact = int(new_contact)
                except ValueError:
                    print("Invalid contact. Skipping update.")

            new_symptom = input("Enter new symptom: ")
            if new_symptom:
                today = datetime.datetime.now().strftime("%Y-%m-%d")
                patient.symptoms.append(new_symptom)
                patient.visit_hist[today] = patient.visit_hist.get(today, []) + [new_symptom]

            print("Patient updated.")
            return

    print("Patient not found.")


def delete():
    try:
        patient_id = int(input("Enter Patient ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    global patients
    for i, patient in enumerate(patients):
        if patient.patient_id == patient_id:
            del patients[i]
            print("Patient deleted.")
            return
    print("Patient not found.")


def menu():
    while True:
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Exit")
        choice = input("Enter your choice : ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patient()
        elif choice == '3':
            search()
        elif choice == '4':
            update()
        elif choice == '5':
            delete()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

menu()
