from data import BIG_DATA as DATA

list1 = DATA[::2]
list2 = DATA[1::2]

diff = []

list1.sort()
list2.sort()

for i in range(len(list1)):
    if list1[i] > list2[i]:
        diff.append(list1[i] - list2[i])
    else:
        diff.append(list2[i] - list1[i])

print(sum(diff))