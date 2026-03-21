
from office import Office
from employee import Employee
from car import Car
from dbManager import save_db

def runEmployee(employee):
   isRunning = True
   while isRunning:
      print("""
            1) Sleep
            2) Eat
            3) Buy
            4) Refuel
            5) Drive
            6) Send Email
            7) Work
            8) Check Health
            9) Check Mood
            0) Back to office
            """)
      try:
        choice = input("Enter your choice: ")
        if choice == "1":
            hours = input("Enter hours: ")
            employee.sleep(hours)
        elif choice == "2":
            meals = input("Enter meals: ")
            employee.eat(meals)
        elif choice == "3":
            items = input("Enter items: ")
            employee.buy(items)
        elif choice == "4":
            gas = input("Enter gas: ")
            employee.refuel(gas)
        elif choice == "5":
            distance = input("Enter distance: ")
            velocity = input("Enter velocity: ")
            employee.drive(distance,velocity)
        elif choice == "6":
            subject = input("Enter subject: ")
            message = input("Enter message: ")
            reciver_name = input("Enter reciver name: ")
            employee.send_email(subject,message,reciver_name)
        elif choice == "7":
            hours = input("Enter hours: ")
            employee.work(hours)
        elif choice == "8":
            employee.check_health()
        elif choice == "9":
            employee.check_mood()
        elif choice == "0":
            isRunning = False
        else:
            raise ValueError("Invalid choice")
      except Exception as e:
        print(e)

def runOffice():
  
  isRunning = True
  while isRunning:
      print("""
          1) Hire Employee
          2) display employees
          3) display employee by id
          4) Fire Employee
          5) Check Lateness
          6) Deduct from Employee
          6) Reward Employee
          8) Save Database
          9) Connect to Employee
          0) Exit
            """)
      try:
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter employee name: ")
            money=input("Enter employee money: ")
            mood=input("Enter employee mood: ")
            healthRate=input("Enter employee healthRate: ")
            car_name=input("Enter employee car name: ")
            car_fuelRate=input("Enter employee car fuelRate: ")
            car_velocity=input("Enter employee car velocity: ")
            car = Car(car_name,car_fuelRate,car_velocity)
            email=input("Enter employee email: ")
            salary=input("Enter employee salary: ")
            distanceToWork=input("Enter employee distanceToWork: ")
            employee = Employee(name,money,mood,healthRate,car,email,salary,distanceToWork)
            office.hire(employee)
        elif choice == "2":
            employees = office.get_all_employees()
            for employee in employees:
                print(employee)
        elif choice == "3":
            employee_id = input("Enter employee id: ")
            print(office.get_employee_by_id(employee_id))
        elif choice == "4":
            employee_id = input("Enter employee id: ")
            office.fire_by_id(employee_id)
        elif choice == "5":
            employee_id = input("Enter employee id: ")
            moveHour = input("Enter moveHour: ")
            office.check_lateness(employee_id,moveHour)
        elif choice == "6":
            employee_id = input("Enter employee id: ")
            deduction = input("Enter deduction: ")
            office.deduct(employee_id,deduction)
        elif choice == "7":
            employee_id = input("Enter employee id: ")
            reward = input("Enter reward: ")
            office.reward(employee_id,reward)
        elif choice == "8":
            save_db(office)
        elif choice == "9":
            employee_id = input("Enter employee id: ")
            runEmployee(office.get_employee_by_id(employee_id))
        elif choice == "0":
            isRunning = False
        else:
            raise ValueError("Invalid choice")
      except Exception as e:
        print(e)

office = Office("ITI",[])
runOffice()