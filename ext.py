class car:
  def __init__(self, make, model, varient):
    self.make = make
    self.model = model
    self.varient = varient

  def __str__(self):
    return f'The {self.make} {self.model}\'s {self.varient}'

  def move(self,make,model):
    return f'The {self.make} {self.model} is moving'

class seats(car):
  def __init__(self,make,model,varient,type):
    super().__init__(make,model,varient)
    self.type = type

  def __str__(self):
    return f'The {self.make} {self.model}\'s {self.varient} has {self.type} seats'


class plane:
  def __init__(self,make,model):
    self.make = make  
    self.model = model

  def move(self,make,model):
    return f'The {self.make} {self.model} is moving'

class bike:
  def __init__(self,make,model):
    self.make = make  
    self.model = model

  def move(self,make,model):
    return f'The {self.make} {self.model} is moving'

