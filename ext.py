class car:
  def __init__(self, make, model, varient):
    self.make = make
    self.model = model
    self.varient = varient

  def __str__(self):
    return f'The {self.make} {self.model}\'s {self.varient}'

class seats(car):
  def __init__(self,make,model,varient,type):
    super.__init__(make,model,varient)
    self.type = type