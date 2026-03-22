import validator
from constants import Mood,HealthRatePercentage,ITEM_COST,IDEAL_SLEEP_HOURS,IDEAL_MEALS
class Person:
    def __init__(self, name,money,mood,healthRate):
        if not validator.isAlpha(name):
            raise TypeError("Invalid name")
        if not validator.isFloat(money):
            raise TypeError("Invalid money")
        if not validator.isPostive(money):
            raise ValueError("money cannot be negative")
        if not validator.isMood(mood):
            raise TypeError("Invalid mood")
        if not validator.isFloat(healthRate):
            raise TypeError("Invalid healthRate")
        if not validator.isValidRange(healthRate,HealthRatePercentage.NO_HEALTH.value,HealthRatePercentage.FULL_HEALTH.value):
            raise ValueError("healthRate is out of range")
        
        money = float(money)
        self.__name = name
        self.__money = money
        self.__mood = mood
        self.__healthRate = healthRate

    @property
    def name(self):
        return self.__name
    @property
    def money(self):
        return self.__money
    @property
    def mood(self):
        return self.__mood
    @property
    def healthRate(self):
        return self.__healthRate

    @name.setter
    def name(self,name):
        if not validator.isAlpha(name):
            raise TypeError("Invalid name")
        self.__name = name
    @money.setter
    def money(self,money):
        if not validator.isFloat(money):
            raise TypeError("Invalid money")
        if not validator.isPostive(money):
            raise ValueError("money cannot be negative")
        
        money = float(money)
        self.__money = money
    @mood.setter
    def mood(self,mood):
        if not validator.isMood(mood):
            raise TypeError("Invalid mood")
        self.__mood = mood
    @healthRate.setter
    def healthRate(self,healthRate):
        if not validator.isFloat(healthRate):
            raise TypeError("Invalid healthRate")
        if not validator.isValidRange(healthRate,HealthRatePercentage.NO_HEALTH.value,HealthRatePercentage.FULL_HEALTH.value):
            raise ValueError("healthRate is out of range")
        self.__healthRate = healthRate


    def sleep(self,hours):
      if not validator.isFloat(hours):
          raise TypeError("invalid hours")
      if not validator.isPostive(hours):
        raise ValueError("hours must be postive")
      hours = float(hours)
      if hours == IDEAL_SLEEP_HOURS:
          self.__mood = Mood.HAPPY.name.lower()
      elif hours > IDEAL_SLEEP_HOURS:
          self.__mood = Mood.LAZY.name.lower()
      else:
          self.__mood = Mood.TIRED.name.lower()
          


    def eat(self,meals):
      if not validator.isNumber(meals):
        raise TypeError("invalid meals")
      if not validator.isPostive(meals):
         raise ValueError("hours must be postive")
      meals = int(meals)
      if meals == IDEAL_MEALS:
        self.__healthRate = HealthRatePercentage.FULL_HEALTH.value
      elif meals == IDEAL_MEALS-1:
        self.__healthRate = HealthRatePercentage.THREE_QUARTERS_HEALTH.value
      else:
        self.__healthRate = HealthRatePercentage.HALF_HEALTH.value
      
        
    def buy(self,items):
      if not validator.isNumber(items):
        raise TypeError("invalid items")
      
      items = int(items)
      money_check = 0
      for i in range(0,items):
        money_check+=ITEM_COST
      
      if self.__money - money_check < 0:
        raise ValueError("not enough money")
      else:
        self.__money -= money_check