price = 3
money = 20
count = 4

totalAmt = 0
for i in range(1, count + 1):
    totalAmt += (price * i)
    
if (totalAmt > money):
    answer = totalAmt - money
else:
    answer = 0

print(answer) 