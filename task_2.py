#task
amount=float(input("enter purchaase amount"))
if amount<0:
    print("invalid amount")
else:
    discount=0.0
    if amount>=5000:
        discount=amount*20/100
    elif amount>=2000 and amount<5000:
        discount=amount*10/100
    elif amount<2000:
        no discount 
#task
temperature=float(input("enter the temperature: "))
if temperature<20:
    print("cold")
elif temperature>=20 and temperature<30:
    print("pleasant")
elif temperature>=30 and temperature<40:
    print("hot")
else:
    print("very hot")            
