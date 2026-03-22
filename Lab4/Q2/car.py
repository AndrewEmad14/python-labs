import validator
from constants import MAX_FUEL_RATE,MIN_FUEL_RATE,MAX_VELOCITY,MIN_VELOCITY
class Car:

  def __init__(self,name,fuelRate,velocity):
    if not validator.isAlnum(name):
      raise TypeError("Invalid name")
    if not validator.isFloat(fuelRate):
      raise TypeError("Invalid fuelRate")
    if not validator.isValidRange(fuelRate,MIN_FUEL_RATE,MAX_FUEL_RATE):
      raise ValueError(f"Fuel rate has to be between {MIN_FUEL_RATE} and {MAX_FUEL_RATE}")
    if not validator.isFloat(velocity):
      raise TypeError("Invalid velocity")
    if not validator.isValidRange(velocity,MIN_VELOCITY,MAX_VELOCITY):
      raise ValueError(f"Velocity has to be between {MIN_VELOCITY} and {MAX_VELOCITY}")
    
    self.__name = name
    fuelRate = float(fuelRate)
    velocity = float(velocity)
    self.__fuelRate = fuelRate
    self.__velocity = velocity

  @property
  def name(self):
    return self.__name
  
  @property
  def fuelRate(self):
    return self.__fuelRate
  
  @property
  def velocity(self):
    return self.__velocity
  
  @name.setter
  def name(self,name):
    if not validator.isAlnum(name):
      raise TypeError("Invalid name")
    self.__name = name

  @fuelRate.setter
  def fuelRate(self,fuelRate):
    if not validator.isFloat(fuelRate):
      raise TypeError("Invalid fuelRate")
    if not validator.isValidRange(fuelRate,MIN_FUEL_RATE,MAX_FUEL_RATE):
      raise ValueError(f"Fuel rate has to be between {MIN_FUEL_RATE} and {MAX_FUEL_RATE}")
    
    fuelRate = float(fuelRate)
    self.__fuelRate = fuelRate

  @velocity.setter
  def velocity(self,velocity):
    if not validator.isFloat(velocity):
      raise TypeError("Invalid velocity")
    if not validator.isValidRange(velocity,MIN_VELOCITY,MAX_VELOCITY):
      raise ValueError(f"Velocity has to be between {MIN_VELOCITY} and {MAX_VELOCITY}")
    
    velocity = float(velocity)

    self.__velocity = velocity

  def run(self, distance, velocity):
    self.velocity = velocity
    
   
    fuel_needed = distance * velocity 
    remaining_fuel = self.fuelRate - fuel_needed
    
    self.fuelRate = remaining_fuel if remaining_fuel >= 0 else 0
    
    if remaining_fuel > 0:
        remaining_distance = 0
    else:
        remaining_distance = remaining_fuel / velocity 
    
    self.stop(remaining_distance)
      

  def stop(self,remainigDistance):
    self.velocity = 0
    if remainigDistance == 0:
      print("You have arrived at your destenation")
    else:
      print(f"You have run out of fuel! You have {remainigDistance} km left to your destenation")
  