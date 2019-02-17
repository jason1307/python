import math

def primeFactors(n):


    while n % 2 == 0:
        print (2)
        n = n / 2

    for i in range(3,int(math.sqrt(n))+1,2):


        while n % i== 0:
            print (i)
            n = n / i

    if n > 2:
        print (n)

a=0
while a==0:

    user_number = input ("Παρακαλω εισαγετε εναν ακεραιο μεταξυ 0-1000000!")
    try:
        val = int(user_number)
        if val in range(0,1000000):
            a=1
            n= val
        else:
            print("Ο αριθμος πρεπει να ειναι μεταξυ 0-1000000!")

    except ValueError:
            print("Πρεπει να ειναι αριθμος και ακεραιος!")

            
primeFactors(n)
