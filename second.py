class FirstClass: 
     def setdata(self, value): 
         self.data = value 
     def display(self):
         print(self.data) 
         
         


x = FirstClass() 
y = FirstClass() 


print(x)
print(y)
print(isinstance(x, FirstClass))

print("##########################")

x.setdata("Ahmed") 
y.setdata(3.14159) 
x.display()
y.display()

print("##########################")

x.data = "New value" # Can set attributes
x.display()

print("##########################")

x.anothername = "spam" # Can set new attributes 
print(x.anothername)
