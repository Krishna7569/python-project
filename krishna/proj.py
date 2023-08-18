from datetime import datetime
name=input('Customer name:')
#list of items
lists='''
Rice      Rs.20/kg
Sugar     Rs.40/kg
Jeera     Rs.30/kg
Tamarind  Rs.50/kg
Tomato    Rs.30/kg
Boost     Rs.45/kg
Water     Rs.2/lit
Wheat     Rs.56/kg
'''
#declaration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
# rates for items
items={'Rice':20,'Sugar':40,'Jeera':30,'Tamarind':50,'Tomato':30,'Boost':45,'Water':2,'Wheat':56}
op=int(input('for list of items press 1:'))
if(op==1):
    print(lists) 
for i in range(len(items)):
    inp1=eval(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items:")
        quantity=int(input("enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry entered item is not available")
        inp=input("want to bill item yes or no:")
        if inp=='yes':
            pass
        if finalamount!=0:
            print(25*" ","Banglore")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(70*"-")
            print("sno",8*" ",'items',8*" ","quantity",3*' ',"price")
            for i in range(len(pricelist)):
                print(i,8*' ',8*' ',ilist[i],3*' ',qlist[i],plist[i])
            print(70*"-")
            print(20*' ','TotalAmount:','Rs',finalamount)
            print(70*"-")
            print(40*" ",'Thanks for visiting')
            print(70*"-")