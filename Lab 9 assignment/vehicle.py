class Vehicle:
  def __init__ (self,plate,brand,model,year,daily_rate):
    self.plate=plate
    self.brand=brand
    self.model=model
    self.year=year
    self.daily_rate=daily_rate
  def show(self):
    return [self.plate,self.brand,self.model,self.year,self.daily_rate]
    
class Car(Vehicle):
  def __init__(self,plate,brand,model,year,daily_rate,seat):
    super().__init__ (plate,brand,model,year,daily_rate)
    self.seat=seat
  def show(self):
    return super().show()+[self.seat]
    
class Truck(Vehicle):
  def __init__ (self,plate,brand,model,year,daily_rate,payload):
    super().__init__ (plate,brand,model,year,daily_rate)
    self.payload=payload
  def show(self):
    return super().show()+[self.payload]

def calculate_rental_cost(vehi,rent,car,truck):
  count=0
  if vehi=='car':
    print(f'ทะเบียน:\t{car[0]}\nยี่ห้อ:\t{car[1]}\nรุ่น:\t\t{car[2]}\nปี:\t\t{car[3]}\nค่าเช่า:\t{car[4]}\nที่นั่ง:\t{car[5]}')
    if rent>=5:
      while rent>=5:
        rent-=5
        count+=1
      print(f'{'*'*20}\nค่าเช่ารวม:\t{car[4]*count*5} baht\nแถม:\t\t{count*2} วัน\n{'*'*20}')
    else:
      print(f'{'*'*20}\nค่าเช่ารวม:\t{car[4]*rent} baht\nแถม:\t\t{count*2} วัน\n{'*'*20}')
  elif vehi=='truck':
    print(f'ทะเบียน:\t{truck[0]}\nยี่ห้อ:\t{truck[1]}\nรุ่น:\t\t{truck[2]}\nปี:\t\t{truck[3]}\nค่าเช่า:\t{truck[4]}\nบรรจุ(ตัน):\t{truck[5]}')
    if rent>=5:
      while rent>=5:
        rent-=5
        count+=1
      print(f'{'*'*20}\nค่าเช่ารวม:\t{truck[4]*count*5} baht\nแถม:\t\t{count*2} วัน\n{'*'*20}')
    else:
      print(f'{'*'*20}\nค่าเช่ารวม:\t{truck[4]*rent} baht\nแถม:\t\t{count*2} วัน\n{'*'*20}')
  else:
    print('car and truck only')
    
c=Car('1กก9999 กรุงเทพ','Lamboghini','Urus',2022,90000,5)
t=Truck('72-8888 ชลบุรี','Isuzu','FTR 240',2022,8000,16)
while True:
  try:
    vehi=input('vehile:\t')
    rent=int(input('rent:\t'))
    car=c.show()
    truck=t.show()
    calculate_rental_cost(vehi,rent,car,truck)
  except Exception as a:
    print(f'{a}\n***pls try again***')