# Find The Greatest common divisor


num1 = int(input("Enter First Number :"))
num2 = int(input("Enter Second Number: "))

list1 = 0

for i in range(1,min(num1,num2)):
    if num1 % i == 0 and num2 %i ==0:
        list1 = i

print(list1)

# print(list1[-1])
