largest = None
smallest = None
while True:
    n = input("Enter a number: ")
    if n == "done" :
        break
    try:
        #try block
        num = int(n)    
    except:
        #exception
        print("Invalid input")
        
    if largest == None:
        largest = num
    else:
        if num > largest :
            largest = num
    
    if smallest == None:
        smallest = num
    else:    
        if num < smallest :
            smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)