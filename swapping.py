num1 = int(input("Enter First Number: ")) # 5
num2 = int(input("Enter Second Number: ")) # 6
print ("using multiple varible assignment : ")
num1, num2 = num2, num1
print("Num1: ", num1,"\n","Num2: ", num2)
print ("Using third variable : ")
temp = num1
num1 = num2
num2 = temp
print("Num1: ", num1,"\n","Num2: ", num2)
print("Without using third variable : ")
num1 = num1 + num2
num2 = num1 - num2 
num1 = num1 - num2 

print("Num1: ", num1,"\n","Num2: ", num2)

