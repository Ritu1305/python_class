class Car():


  def __init__(self, model, color, company, speed_limit):
    self.model = model
    self.color = color

    self.company = company
    self.speed_limit = speed_limit
    

  def start(self):
    if self.color == "red":
      print("its my car")
    else:
      print("still my car")

  def stop(self):
    print("stopped")

  def accelarate(self):
    print("accelarating...")
    

  def change_gear(self, gear_type):
    print("gear changed")
   

audi = Car("A6", "blue", "audi", 80)
audi.start()
