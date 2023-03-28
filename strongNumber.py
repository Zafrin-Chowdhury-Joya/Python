def strong(num):
    sum =0
    temp = num
    while (num>0):
        fact = 1
        rem = num % 10
        for i in range (1,rem+1):
            fact = fact *i
        sum = sum + fact
        num = num // 10
    if (sum == temp):
        print ("Strong Number")
    else :
        print("Not a strong number")
num = int (input ("Enter Number = "))
strong (num)