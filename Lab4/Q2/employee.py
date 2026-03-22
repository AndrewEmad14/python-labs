from person import Person
from car import Car
import validator
from constants import Mood,IDEAL_WORK_HOURS,MIN_SALARY,MAX_SALARY

class Employee(Person):
  latestId = 0
  def __init__(self,name,money,mood,healthRate,email,salary,distanceToWork,car,id=-1):
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

    if id != -1:
      if not validator.isNumber(id) and validator.isPostive(id):
        raise TypeError("Invalid id")
      id = int(id)
      self.__id = id
    else:
      self.__id = Employee.latestId + 1
    Employee.latestId = self.__id
    salary = float(salary)
    distanceToWork = float(distanceToWork)
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
    if not validator.isIntanceOf(car,Car):
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
    salary =float(salary)
    self.__salary = salary

  @distanceToWork.setter
  def distanceToWork(self,distanceToWork):
    if not validator.isFloat(distanceToWork):
      raise TypeError("Invalid distanceToWork")
    distanceToWork = float(distanceToWork)
    self.__distanceToWork = distanceToWork

  def work(self,hours):
    if not validator.isFloat(hours):
        raise TypeError("invalid hours")
    
    hours = float(hours)
    if hours == IDEAL_WORK_HOURS:
        self.__mood = Mood.HAPPY.name.lower()
    elif hours < IDEAL_WORK_HOURS:
        self.__mood = Mood.LAZY.name.lower()
    else:
        self.__mood = Mood.TIRED.name.lower()
  def drive(self,distance,velocity):
    if not validator.isFloat(distance) or not validator.isPostive(distance):
      raise TypeError("Invalid distance")
    if not validator.isFloat(velocity) or not validator.isPostive(velocity):
      raise TypeError("Invalid velocity")
    distance = float(distance)
    velocity = float(velocity)
    self.__car.run(distance,velocity)
  def refuel(self,gasAmount=100):
    self.__car.fuelRate = gasAmount
  def sendEmail(self,subject,msg,reciver_name):
    with open(f"to:{reciver_name}.txt","w") as f:
      f.write(f"from:{self.__email}\nto:{reciver_name}\nsubject:{subject}\n{msg}")

  def __str__(self):
            return f"{self.__id}:{self.name}:{self.money}:{self.mood}:{self.healthRate}:{self.email}:{self.salary}:{self.distanceToWork}:{self.car.name}:{self.car.fuelRate}:{self.car.fuelRate}:{self.car.velocity}\n"