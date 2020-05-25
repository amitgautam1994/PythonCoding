n = int(input())

# m = N*3


for i in range(n//2):
    print("---"*((n//2)-i) + ".|."*(i+1) + "---"*((n//2)-i))