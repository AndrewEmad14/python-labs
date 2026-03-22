import validator
from employee import Employee
from constants import TARGET_HOUR,DEDUCTION,REWARD
class Office:
  employeesNum = 0
  def __init__(self,name,employees):
    if not validator.isAlnum(name):
      raise TypeError("Invalid name")
    
    self.__name = name
    self.__employees = employees
    self.employeesNum = len(employees)

  @property
  def name(self):
    return self.__name
  
  @property
  def employees(self):
    return self.__employees
  
  @name.setter
  def name(self,name):
    if validator.isAlnum(name):
      raise TypeError("Invalid name")
    self.__name = name
  
  def get_all_employees(self):
    return self.__employees
  
  def get_employee_by_id(self,id):
    if not validator.isNumber(id) and validator.isPostive(id):
      raise TypeError("Invalid id")
    id = int(id)
    return next((e for e in self.employees if e.id == id) ,None)
  
  def hire(self,employee):
    if not validator.isIntanceOf(employee,Employee):
      raise("invaild employee")
    self.__employees.append(employee)
    Office.__change_num_of_employees(self)

  def fire_by_id(self,id):
    if not validator.isNumber(id) and validator.isPostive(id):
      raise TypeError("Invalid id")
    id = int(id)
    self.__employees = list(filter(lambda emp:emp.id != id , self.__employees))
    Office.__change_num_of_employees(self)
    

    

  def deduct(self,id,deduction):
    if not validator.isNumber(id) and validator.isPostive(id):
      raise TypeError("Invalid id")
    if not validator.isFloat(deduction):
      raise TypeError("Invalid deduction")
    deduction = float(deduction)
    employee = self.get_employee_by_id(id);
    if employee is None:
      raise ValueError("employee not found")
    deducted_salary = employee.salary - deduction
    if not validator.isPostive(deducted_salary):
      raise ValueError("salary cannot be negative")
    employee.salary = deducted_salary
      
  
  def check_lateness (self,id, moveHour):
    if not validator.isFloat(moveHour):
      raise TypeError("Invalid moveHour")
    if not validator.isNumber(id) and validator.isPostive(id):
      raise TypeError("Invalid id")
    employee = self.get_employee_by_id(id);
    if employee is None:
      raise ValueError("employee not found")
    
    moveHour = float(moveHour)
    latness = self.calculate_lateness(TARGET_HOUR, moveHour, employee.distanceToWork, employee.car.velocity)
    if latness > 0:
      self.deduct(id, DEDUCTION)
    else:
      self.reward(id, REWARD)

  def reward(self,id,reward):
    if not validator.isNumber(id) and validator.isPostive(id):
      raise TypeError("Invalid id")
    if not validator.isFloat(reward):
      raise TypeError("Invalid reward")
    reward = float(reward)
    employee = self.get_employee_by_id(id);
    if employee is None:
      raise ValueError("employee not found")
    employee.salary += reward

  @staticmethod
  def calculate_lateness (targetHour , moveHour, distance, velocity):
    time = distance / velocity
    actualHour = moveHour + time
    return actualHour - targetHour
  
  @staticmethod
  def __change_num_of_employees(self):
    self.employeesNum = len(self.__employees)