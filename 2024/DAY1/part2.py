from data import BIG_DATA

list1 = BIG_DATA[::2]
list2 = BIG_DATA[1::2]

simmilarity_score = 0;

list1.sort()
list2.sort()

for number in list1:
    total = list2.count(number)
    simmilarity_score += number * total
    
print(simmilarity_score)