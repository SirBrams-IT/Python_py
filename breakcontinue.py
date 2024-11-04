#Breakk statement -loops stops

num = 20
while num <= 25:
    print(num)
    if num == 23:
        break
    num += 1

#Continue statement- it skips
devices = ["Laptop","Phone","Tablet"]
for x in devices:
    if x=="Phone":
        continue
    print(x)