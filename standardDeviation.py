data = [1,2,3,4,5]
n = len(data)
print(data)
mean = sum(data) / n
print("Mean of Numbers =",mean)
v = sum((x - mean) ** 2 for x in data) / n
deviation = v ** 0.5
print("Standard Deviation =",deviation)
