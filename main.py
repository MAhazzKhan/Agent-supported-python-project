from ext import *
new = car("Ford","Mustang","GT3")
a = new.make
del new.model
del new.varient


new2 = car(new.make,"F-250","Raptor-R")
new3 = seats(new2.make ,new2.model ,new2.varient ,"carbon fiber bucket")

print(new3)


car1 = new2
plane1 = plane("Boeing","747")
bike1 = bike("Kawasaki","ninja H2R")

for i in(car1,plane1,bike1):
  print(i.make,i.model)
