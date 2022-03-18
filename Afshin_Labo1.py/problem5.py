from unicodedata import decimal


def multiplier_et_diviser( p1,p2,p3):
    return((p1*p2)/p3)

p1=decimal(7.250)
p2=decimal(10.725)
p3=decimal(2.256)

print(multiplier_et_diviser(p1,p2,p3)) 

