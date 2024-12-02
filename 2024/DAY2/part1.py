data = open("data","r").readlines()

# split each line into words
# convert each string to an integer
# create a list of lists of integers
data = list(map(lambda y: list(map(lambda x: int(x),y)),list(map(lambda x: x.split(),data))))

# initialize counter for safe reports
safe_reports = 0

for line in data:
    # check if the line is monotonic
    direction = (line==sorted(line)) or (line==sorted(line,reverse=True))
    
    # track if all adjacent differences are valid
    control = True
    
    for i in range(len(line)-1):
        difference = abs(line[i]-line[i+1])
        
        if not 1<=difference<=3:
            control = False
    
    if direction and control:
        safe_reports += 1

print(safe_reports)