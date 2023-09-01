from ext import *
new = car("Ford","Mustang","GT3")
a = new.make
del new.model
del new.varient


new2 = car(new.make,"F-250","Raptor-R")
new3 = seats(new2.make ,new2.model ,new2.varient ,"carbon fiber bucket")

print(new3)
