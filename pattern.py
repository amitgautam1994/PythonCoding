# Pattern Print
def pattern(n)
    n = int(input())

    for i in range(n//2):
        return "---"*((n//2)-i) + ".|."*(i+1) + "---"*((n//2)-i)
