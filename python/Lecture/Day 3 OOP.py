from _typeshed import Self


class Employee:
    def __init__(self, firstName, lastName, employeeId, email, hireDate):
        self.firstName = firstName
        self.lastName = lastName
        self.employeeId = employeeId
        self.email = email
        self.hireDate = hireDate

    def welcomeEmployee(self):
        print(f"Welcome to our company {self.firstName} {self.lastName}!")
        return self

    def printEmployeeInfo(self):
        print(f"{self.firstName} was hired on {self.hireDate}, with an email address of {self.email}")
        return self
class Park:
    ourOrganization = "Unpaid Workers Association"
    

    def __init__(self, parkName, location, parkType, tickets, hours, parking):
        self.parkName = parkName
        self.location = location
        self.shops = []
        self.attractions = []
        self.parkType = parkType
        self.tickets = tickets
        self.hours = hours
        self.parking = parking
        self.animals = []
        self.plants = []
        self.employees = []
    
    def welcome(self):
        print(f"Welcome to {self.parkName}. We are a(n) {self.parkType}, located in {self.location}. the cost to enter is {self.tickets}. At this time our hours of operation are {self.hours}. We have the following parking accoommodations, {self.parking}")

    def addShop(self, shopType):
        self.shops.append(shopType)
    
    def listShops(self):
        print(f"Here are the different shops that we have onsite: {self.shops}")

    
    def addEmployee(self, employee):
        self.employees.append(employee)

    def listEmployees(self):
        print(f"Here is a list of the staff at {self.parkName}. {self.employees[0].firstName}")

claude = Employee("Claude","Will",1,"claude@email.com","April 9th, 2021")
bob = Employee("Bob","Woodward",2,"bob@email.com","September 15th, 2021")
park01 = Park("Lego Land","San Diego, CA","Amusement Park", 300, "8am - 10pm Tuesdays, Thursdays, & Sundays","1st come 1st server")
park02 = Park("Zootopia","Icelandia","Zoo",50,"10am - 10pm 7 Days a week", "7 dedicated locations for parking")

# claude.welcomeEmployee()
# bob.welcomeEmployee()

park01.addShop("Ice Cream Parlor")
park01.addShop("Food Shoppe")
park01.addShop("Lego Land Store")

park01.listShops()