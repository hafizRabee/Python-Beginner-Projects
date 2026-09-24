def currencyconverter(sourcecurrency,targetedcurrency,amount):
    currencycodes=["usd","pkr","cny","inr","cad","jpy","aed","bdt","rub","gbp","krw","chf","aud","sar"]
    if(sourcecurrency not in currencycodes):
      return "invalidsource"
    elif(targetedcurrency not in currencycodes):
      return "invalidtarget"
    elif(sourcecurrency=="usd" and targetedcurrency=="pkr"):
        return amount*277.97
    elif(sourcecurrency=="pkr" and targetedcurrency=="usd"):
        return amount/277.97
    elif(sourcecurrency=="cny" and targetedcurrency=="pkr"):
        return amount*40.91
    elif(sourcecurrency=="pkr" and targetedcurrency=="cny"):
        return amount/40.91
   
     
    elif(sourcecurrency=="inr" and targetedcurrency=="pkr"):
        return amount*2.93
    elif(sourcecurrency=="pkr" and targetedcurrency=="inr"):
        return amount/2.93
    elif(sourcecurrency=="cad" and targetedcurrency=="pkr"):
        return amount*196.05
    elif(sourcecurrency=="pkr" and targetedcurrency=="cad"):
        return amount/196.05
    elif(sourcecurrency=="jpy" and targetedcurrency=="pkr"):
        return amount*1.72
    elif(sourcecurrency=="pkr" and targetedcurrency=="jpy"):
        return amount/1.72
    elif(sourcecurrency=="aed" and targetedcurrency=="pkr"):
        return amount*75.74
    elif(sourcecurrency=="pkr" and targetedcurrency=="aed"):
        return amount/75.74
    elif(sourcecurrency=="bdt" and targetedcurrency=="pkr"):
        return amount*2.26
    elif(sourcecurrency=="pkr" and targetedcurrency=="bdt"):
        return amount/2.26
    elif(sourcecurrency=="rub" and targetedcurrency=="pkr"):
        return amount*3.62
    elif(sourcecurrency=="pkr" and targetedcurrency=="rub"):
        return amount/3.62
    elif(sourcecurrency=="gbp" and targetedcurrency=="pkr"):
        return amount*371.99
    elif(sourcecurrency=="pkr" and targetedcurrency=="gbp"):
        return amount/371.99
    elif(sourcecurrency=="krw" and targetedcurrency=="pkr"):
        return amount*0.18
    elif(sourcecurrency=="pkr" and targetedcurrency=="krw"):
        return amount/0.18
     
    elif(sourcecurrency=="chf" and targetedcurrency=="pkr"):
        return amount*343.49
    elif(sourcecurrency=="pkr" and targetedcurrency=="chf"):
        return amount/343.49
    elif(sourcecurrency=="aud" and targetedcurrency=="pkr"):
        return amount*193.06
    elif(sourcecurrency=="pkr" and targetedcurrency=="aud"):
        return amount/193.06
    elif(sourcecurrency=="sar" and targetedcurrency=="pkr"):
        return amount*74.08
    elif(sourcecurrency=="pkr" and targetedcurrency=="sar"):
        return amount/74.08
    else:
        return "only conversions with pkr are supported"
print(f"===currency converter===")
print('''Available Currencies with their Codes:

USD  - US Dollar:currency code:usd
PKR  - Pakistani Rupee:code:pkr
CNY  - Chinese Yuan code:cny
INR  - Indian Rupee code:inr
CAD  - Canadian Dollar code:cad
JPY  - Japanese Yen code:jpy
AED  - UAE Dirham code:aed
Taka - Bangladeshi Taka code: bdt
RUB  - Russian Ruble code:rub
GBP  - British Pound code: gbp
KRW  - South Korean Won code:krw
CHF  - Swiss Franc code:chf
AUD  - Australian Dollar code:aud
SAR  - Saudi Riyal code:sar''')
print("Note:All conversion supported to/from pkr only")
try:
  amount=float(input("enter amount:"))
  sourcecurrency=input("enter source currency code:").lower()
  targetedcurrency=input("enter target currency code:").lower()
  

  Result=currencyconverter(sourcecurrency,targetedcurrency,amount)
  if(Result=="invalidsource"):
    print("please enter valid source currency code")
  elif(Result=="invalidtarget"):
    print("please enter valid target currency code")
  elif(Result=="only conversions with pkr are supported"):
      print(Result)

  else:

   print(f"{sourcecurrency} to {targetedcurrency}:{Result:.2f}")
except ValueError:
  print("please enter  valid amount")

 
  

     






     






     



