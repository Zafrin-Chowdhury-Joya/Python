num = int(input("Range of prime numbers = "))
sum = 0
print("prime numbers =")
if num > 1:
    for i in range (2,num+1):
        for j in range (2,i):
            if(i%j) == 0:
                break

        else :
           print(i)
           sum+=i
print("Summation of prime numbers = ",sum)
