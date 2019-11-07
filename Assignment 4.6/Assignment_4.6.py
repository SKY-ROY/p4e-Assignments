def computepay(h,r):
    if h>40:
        #pay for 40+ hours
        hn = h-40
        pay = (r*40) + (hn*r*1.5)
    else:
        #pay for upto 40 hours
        pay = h*r
    return pay
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(float(hrs),float(rate))
print(p)