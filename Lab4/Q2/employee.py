from person import Person
from car import Car
import validator
from constants import Mood,HealthRatePercentage,IDEAL_WORK_HOURS,MIN_SALARY,MAX_SALARY

class Employee(Person):
  latestId = 0
  def __init__(self, name,money,mood,healthRate,car,email,salary,distanceToWork):
    super().__init__(name,money,mood,healthRate)
    
    if not validator.isIntanceOf(car,Car):
      raise TypeError("Invalid car")
    if not validator.isEmail(email):
      raise TypeError("Invalid email")
    if not validator.isFloat(salary):
      raise TypeError("Invalid salary")
    if not validator.isValidRange(salary,MIN_SALARY,MAX_SALARY):
      raise ValueError("salary must be more than 1000 and less than 1000000")
    if not validator.isFloat(distanceToWork):
      raise TypeError("Invalid distanceToWork")


    self.__id = Employee.latestId + 1
    Employee.latestId = self.id

    self.__car = car
    self.__email = email
    self.__salary = salary
    self.__distanceToWork = distanceToWork

  @property
  def id(self):
    return self.__id
  
  @property
  def car(self):
    return self.__car
  
  @property
  def email(self):
    return self.__email
  
  @property
  def salary(self):
    return self.__salary
  
  @property
  def distanceToWork(self):
    return self.__distanceToWork
  
  @car.setter
  def car(self,car):
    if validator.isIntanceOf(car,Car):
      raise TypeError("Invalid car")
    self.__car = car

  @email.setter
  def email(self,email):
    if not validator.isEmail(email):
      raise TypeError("Invalid email")
    self.__email = email

  @salary.setter
  def salary(self,salary):
    if not validator.isFloat(salary):
      raise TypeError("Invalid salary")
    if not validator.isValidRange(salary,MIN_SALARY,MAX_SALARY):
      raise ValueError("salary must be more than 1000 and less than 1000000")
    self.__salary = salary

  @distanceToWork.setter
  def distanceToWork(self,distanceToWork):
    if not validator.isFloat(distanceToWork):
      raise TypeError("Invalid distanceToWork")
    self.__distanceToWork = distanceToWork

  def work(self,hours):
    if not validator.isFloat(hours):
        raise TypeError("invalid hours")
    
    hours = float(hours)
    if hours == IDEAL_WORK_HOURS:
        self.__mood = Mood.happy
    elif hours < IDEAL_WORK_HOURS:
        self.__mood = Mood.lazy
    else:
        self.__mood = Mood.tired
  def drive(self,distance,velocity):
    self.__car.run(self,distance,velocity)
  def refuel(self,gasAmount=100):
    self.__car.fuelRate = gasAmount
  def sendEmail(self,subject,msg,reciver_name):
    with open(f"to:{reciver_name}","w") as f:
      f.write(f"from:{self.__email}to:{reciver_name}\nsubject:{subject}\nmsg:{msg}")

  def __str__(self):
            return f"{self.__id}:{self.name}:{self.money}:{self.mood}:{self.healthRate}:{self.email}:{self.salary}:{self.distanceToWork}:{self.car.velocity}\n"