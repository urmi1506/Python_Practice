from prettytable import PrettyTable


class Hospital:
    hospital_name=""
    hospital_reg_no= 0

    def __init__(self,location,departments=None):
        self.location=location
        self.departments=departments if departments else []
        self.hospital_info=[]
    
    def show_info(self):
        t=PrettyTable(['hospital_name','hospital_reg_no','location','departments'])
        for items in self.hospital_info:
            t.add_row([items['hospital_name'],items['hospital_reg_no'],items['location'],",".join(items['departments'])])
        print(t)

    def add_department(self,department):
        self.departments.append(department)
        new_department={
            'hospital_name':self.hospital_name,
            'hospital_reg_no':self.hospital_reg_no,
            'location':self.location,
            'departments':self.departments
        }
        self.hospital_info=[new_department]

    @classmethod
    def update_reg(cls,hospital_reg_no):
        cls.hospital_reg_no = hospital_reg_no


class Doctor:
    doctor_count=0

    def __init__(self,name,specialization,salary):
        self.name=name
        self.specialization=specialization
        self._salary=salary
        self.patient_list=[]
        Doctor.doctor_count +=1

    def add_patient(self,patient_name,patient_age):
        new_patient={
            'patient_name':patient_name,
            'patient_age':patient_age
        }
        self.patient_list.append(new_patient)
    
    def remove_patient(self,patient_name):
        for patient in self.patient_list:
            if patient['patient_name']== patient_name:
                self.patient_list.remove(patient)
                break

    def __getattr__(self,attr):
        if attr == "salary":
            return self._salary
        raise AttributeError(f"Doctor has no attribute {attr}")
    
    def __setattr__(self, attr, value):
        if attr == "salary":
            if value > 0:
                self.__dict__["_salary"] = value
            else:
                print("Invalid salary")
        else:
            super().__setattr__(attr, value)

    def __del__(self):
        print(f"Doctor deleted record :{self.name}")

class Patient:
    def __init__(self,name,age,disease,admitted=False):
        self.name=name
        self.age=age
        self.disease=disease
        self.admitted=admitted
        self._medical_history=[]

    def admit(self):
        self.admitted=True

    def discharge(self):
        self.admitted=False

    def add_medical_record(self, record):
        self._medical_history.append(record)

    def show_info(self):
        t = PrettyTable(['Name', 'Age', 'Disease', 'Admitted'])
        t.add_row([self.name, self.age, self.disease, self.admitted])
        print(t)


class Staff:
    def __init__(self,name,role,salary):
        self.name=name
        self.role=role
        self.salary=salary
        self.staff_info=[]

    def show_staff_info(self):
        print(f"Name: {self.name}, Role: {self.role}, Salary: {self.salary}")

class Nurse(Staff):
    def __init__(self,name ,salary,shift_time):
        super().__init__(name,"Nurse",salary)
        self.shift_time=shift_time

    def assist_doctor(self):
        print(f"Nurse {self.name} is assisting the doctor during {self.shift_time} shift.")


# hospitalInfo
h1 = Hospital("New York")
Hospital.hospital_name = "CityCare Hospital"
Hospital.update_reg(12345)

h1.add_department("Cardiology")
h1.add_department("Neurology")
h1.add_department("Orthopedics")

print("\nHospital Info:")
h1.show_info()

# Doctors
d1 = Doctor("Alice", "Cardiologist", 5000)
d2 = Doctor("Bob", "Neurologist", 6000)

print("\nDoctors:")
print(f"{d1.name} - {d1.specialization}, Salary: {d1.salary}")
print(f"{d2.name} - {d2.specialization}, Salary: {d2.salary}")

d1.salary = 7000
print(f"Updated {d1.name}'s Salary: {d1.salary}")
d1.salary = -1000  # invalid

# Patients
d1.add_patient("John Doe", 45)
d1.add_patient("Jane Smith", 50)
print(f"\n{d1.name}'s Patients: {d1.patient_list}")

d1.remove_patient("John Doe")
print(f"After Removal: {d1.patient_list}")

p1 = Patient("Tom", 30, "Flu")
p1.admit()
p1.add_medical_record("Initial checkup - flu symptoms")
print("\nPatient Info:")
p1.show_info()

# Staff & Nurse
s1 = Staff("Michael", "Receptionist", 3000)
print("\nStaff Info:")
s1.show_staff_info()

n1 = Nurse("Emily", 3500, "Night")
print("\nNurse Info:")
n1.show_staff_info()
n1.assist_doctor()

print(f"\nTotal Doctors: {Doctor.doctor_count}")
