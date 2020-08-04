def computepay(h,r):
    if h <= 40 : 
       h=h*r
       return h
    else :
       extra = h-40
       extra = extra * r * 1.5
       h= (40*r) + extra
       return h

hrs = input("Enter Hours:")
rate = input("enter rate per hour")
h=float(hrs)
r=float(rate)
p = computepay(h,r)
print("Pay",p)