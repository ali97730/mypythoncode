hrs = input("Enter Hours:")
h = float(hrs)
rate = input("enter rate:")
r = float(rate)

if h <= 40 : 
    h=h*r
    print(h)
else :
    extra = h-40
    extra = extra * r * 1.5
    h= (40*r) + extra
    print(h)