# currency converter
class Currency:

  print("\n\nChange your currency")
  def __init__(self,amount,from_currency,to_currency):
    self.amount=amount
    self.from_currency=from_currency
    self.to_currency=to_currency

  def convert(self):
    if self.from_currency=="USD" and self.to_currency=="Taka":
     return self.amount*87.85
    elif self.from_currency=="Dinar" and self.to_currency=="Taka":
      return self.amount*12
    elif self.from_currency=="EUR" and self.to_currency=="Taka":
      return self.amount*91.85    
    elif self.from_currency=="Taka" and self.to_currency=="USD":    
      return self.amount/87.85
    elif self.from_currency=="Taka" and self.to_currency=="Dinar":    
      return self.amount/12
    elif self.from_currency=="Taka" and self.to_currency=="EUR":    
      return self.amount/91.85
 



while True:
  print("\n\n1.USD to Taka --- 2.Dinar to Taka --- 3.EUR to Taka\n4.Taka to USD --- 5.Taka to Dinar --- 6.Taka to EUR --- 0.Exit")
  choice=float(input("\n\n \t\tEnter your choice: "))
  if choice==1:
    amount=float(input("\nEnter amount: "))
    taka=Currency(amount,"USD","Taka")
    print(taka.convert())
  elif choice==2:
    amount=float(input("\nEnter amount: "))
    taka=Currency(amount,"Dinar","Taka")
    print(taka.convert())
  elif choice==3:
    amount=float(input("\nEnter amount: "))
    taka=Currency(amount,"EUR","Taka")
    print(taka.convert())
  elif choice==4:
    amount=float(input("\nEnter amount: "))
    taka=Currency(amount,"Taka","USD")
    print(taka.convert())
  elif choice==5:
    amount=float(input("\nEnter amount: "))
    taka=Currency(amount,"Taka","Dinar")
    print(taka.convert())
  elif choice==6:
    amount=float(input("\nEnter amount: "))
    taka=Currency(amount,"Taka","EUR")
    print(taka.convert())
  elif choice==0 or choice >6:
    break
