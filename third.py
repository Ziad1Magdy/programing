class Customer:
    def __init__(self, name, balance=0):  
        self.name = name
        self.balance = balance
        print("The __init__ method was called")
        
    def __str__(self): 
        return 'Customer: ' + str(self.name) + ', Balance: ' + str(self.balance)
    
    def __add__(self, other): 
        return Customer("Customer", self.balance + other)

    def __del__(self): 
        print('Employee deleted.')    

cust = Customer("Lara de Silva", 100)
print(cust)  
c2 = cust + 230
print(c2.balance)
