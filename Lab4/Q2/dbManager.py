import validator
from office import Office
def save_db(office):
  if not validator.isIntanceOf(Office):
    raise TypeError("invalid office")
  
  employees = office.get_all_employees()

  with open("office.txt","+a") as f:
      for employee in employees:
        f.write(f"{employee.__id}:{employee.name}:{employee.money}:{employee.mood}:{employee.healthRate}:{employee.email}:{employee.salary}:{employee.distanceToWork}:{employee.car.velocity}\n")