

print("Enter operation you wants to perform:")
print("list, set or dictionary\n")

op = input()

if op == "list":
    nums = int(input("Enter size of list"))
    print("Enter Items of list")
    li = [input() for i in range(nums)]
    print(li)

if op == "set":
    nums = int(input("Enter size:"))
    print("Enter Items of list")
    se = {input() for i in range(nums)}
    print(se)

if op == "dictionary":
    it = int(input("lenght of dictionary"))
    print("Enter Items of dictionary")

    dict1 = {i:input() for i in range(it)}

    print(dict1)