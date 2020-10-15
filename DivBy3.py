# num = int(input("Numbers Upto: "))
#
# li = {i for i in range(num) if i%3 == 0}
#
# # for i in range(num +1):
# #     if i%3 == 0:
# #         li.append(i)
#
# print(li)
def DivByThree()
  dict1 = {i:f"Item {i}" for i in range(10)}

  dict2 = {value:key for key,value in dict1.items()}


  print(dict1)
  print(dict2)
