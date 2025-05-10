# currency converter
class Currency:

  print("Change your currency")
  def __init__(self,amount,from_currency,to_currency):
    self.amount=amount
    self.from_currency=from_currency
    self.to_currency=to_currency

  def convert(self):
    if self.from_currency=="USD" and self.to_currency=="Taka":
     return self.amount*87.85
    elif self.from_currency=="Dinar" and self.to_currency=="Taka":
      return self.amount*0.12
    elif self.from_currency=="EUR" and self.to_currency=="Taka":
      return self.amount*91.85    
    elif self.from_currency=="Taka" and self.to_currency=="USD":    
      return self.amount/87.85
    elif self.from_currency=="Taka" and self.to_currency=="Dinar":    
      return self.amount/0.12
    elif self.from_currency=="Taka" and self.to_currency=="EUR":    
      return self.amount/91.85
 



while True:
  print("1.USD to Taka\n2.Dinar to Taka\n3.EUR to Taka\n4.Taka to USD\n5.Taka to Dinar\n6.Taka to EUR\n7.Exit")
  choice=float(input("Enter your choice: "))
  if choice==1:
    amount=float(input("Enter amount: "))
    taka=Currency(amount,"USD","Taka")
    print(taka.convert())
  elif choice==2:
    amount=float(input("Enter amount: "))
    taka=Currency(amount,"Dinar","Taka")
    print(taka.convert())
  elif choice==3:
    amount=float(input("Enter amount: "))
    taka=Currency(amount,"EUR","Taka")
    print(taka.convert())
  elif choice==4:
    amount=float(input("Enter amount: "))
    taka=Currency(amount,"Taka","USD")
    print(taka.convert())
  elif choice==5:
    amount=float(input("Enter amount: "))
    taka=Currency(amount,"Taka","Dinar")
    print(taka.convert())
  elif choice==6:
    amount=float(input("Enter amount: "))
    taka=Currency(amount,"Taka","EUR")
    print(taka.convert())
  elif choice==0:
    break
