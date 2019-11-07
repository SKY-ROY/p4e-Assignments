hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h>40:
    #pay for 40+ hours
    hn = h-40
    pay = (r*40) + (hn*r*1.5)
    print(pay)
else:
    #pay for upto 40 hours
    pay = h*r
    print(pay)