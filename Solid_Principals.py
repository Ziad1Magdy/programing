#Single Responsibility    كل كلاس بيعمل مهمه واحده بس
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class EmployeeRepository:
    def save(self, employee: Employee):
        print(f"Saving employee to database: {employee.name}")


print("##########################################################################")

#Open/Closed Principle     متحاح انك تضيف عليه بس مش متاح التعديل
class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius ** 2


print("##########################################################################")

#Liskov Substitution     ممكن ان الكلاس الفرعي يستبدل بالرئيسي دون من غير ما يعمل ايرور 
class Bird:
    def fly(self):
        print("Bird is flying")

class Sparrow(Bird):
    pass

class Penguin(Bird):
    def fly(self):
        print("Penguins can't fly but they can swim!")


print("##########################################################################")


#Interface Segregation    لازم تقسم المهام الى مهام اصغر علشان لو حبيت تجمع اكتر من مهمه مع بعض يبقى سهل
class Printable:

    def print_content(self):
        pass

class Scannable:
    def scan_content(self):
        pass

class MultiFunctionPrinter(Printable, Scannable):
    def print_content(self):
        print("Printing document...")

    def scan_content(self):
        print("Scanning document...")



print("##########################################################################")

#Dependency Inversion   لازم البرنامج يعتمد على الكلاس الرئيسيه الي مفهاش تفاصيل
class Notification:
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending Email: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")

class NotificationService:
    def __init__(self, notifier: Notification):
        self.notifier = notifier 

    def notify(self, message):
        self.notifier.send(message)



