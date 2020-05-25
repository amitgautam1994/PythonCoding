marksheet = []
scoresheet = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    marksheet.append([name,score])
    scoresheet.append(score)

print(marksheet)
print(scoresheet)

mini  = min(scoresheet)
newlist =[]
for i in scoresheet:
    if i != mini:
        newlist.append(i)

print(newlist)

newlist.sort()

sec = newlist[0]

res =[]

for a,c in marksheet:
    if c == sec:
        res.append(a)

res.sort()

for x in res:
    print(x)