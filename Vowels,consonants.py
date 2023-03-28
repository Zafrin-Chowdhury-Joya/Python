str = input("Enter a string to check = ")
vowels = 0
space =0
consonants = 0
for i in  str :
    if(i=='a'or i =='e'or i == 'o'or i=='i'or i=='u'or i=='A'or i =='E'or i == 'O'or i=='I'or i=='U'):
        vowels += 1
    elif (i ==' '):
        space+=1
    else:
        consonants +=1
print ("Numbers of vowels = ", vowels)
print("Numbers of spaces = ",space)
print("Numbers of consonant = ",consonants)