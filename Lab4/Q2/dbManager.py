import validator
from office import Office
from employee import Employee
from car import Car
def save_db(office):

  if not validator.isIntanceOf(office,Office):
    raise TypeError("invalid office")
  
  employees = office.get_all_employees()
  print(f"Number of employees: {len(employees)}")  # Debug: Check if empty
  with open("office.txt","a") as f:
    for employee in employees:
      print(str(employee))
      f.write(str(employee))

  

def load_db():
  with open("office.txt","r") as f:
    lines = f.readlines()
    employees = []
    for line in lines:
      data = line.split(":")
      car_name=data[8]
      car_fuelRate=data[9]
      car_velocity=data[10]
      car = Car(car_name,car_fuelRate,car_velocity)
      employee = Employee(data[1],data[2],data[3],data[4],data[5],data[6],data[7],car,data[0])
      employees.append(employee)
      
  return employees