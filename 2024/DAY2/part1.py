data = open("testdata","r").readlines()
data = list(map(lambda y: list(map(lambda x: int(x),y)),list(map(lambda x: x.split(),data))))

ans = 0
for line in data:
    direction = (line==sorted(line)) or (line==sorted(line,reverse=True))
    control = True
    for i in range(len(line)-1):
        difference = abs(line[i]-line[i+1])
        if not 1<=difference<=3:
            control = False
    if direction and control:
        ans += 1

print(ans)