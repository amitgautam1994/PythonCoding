# Find The Greatest common divisor


num1 = int(input("Enter First Number :"))
num2 = int(input("Enter Second Number: "))

list1 = []
list2 = []

for i in range(1,num1+1):
    if num1 % i == 0:
        list1.append(i)

for j in range(1,num2+1):
    if num2 % j == 0:
        list2.append(j)

print(list1)
print(list2)

new  = max(set(list1).intersection(set(list2)))

print(new)