P = 11
if P > 1:
    Isprime = True


    for i in range(2, P-1):
        if (P % i) == 0:
           Isprime = False
           break
    
    if Isprime == False:
        print(P, "is not a prime number")
    if Isprime == True:
        print(P, "is a prime number")

else:
     print(P, "is not a prime number")









