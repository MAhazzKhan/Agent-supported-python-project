from ext import car
new = car("Ford","Mustang","GT3")
a = new.make
del new.model
del new.varient


new2 = car(new.make,"F-250","Raptor-R")

print(new2)