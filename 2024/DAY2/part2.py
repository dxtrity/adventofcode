def is_safe_line(line):
    direction = (line == sorted(line)) or (line == sorted(line, reverse=True))
    control = all(1 <= abs(line[i] - line[i+1]) <= 3 for i in range(len(line)-1))
    return direction and control

data = open("data","r").readlines()
data = list(map(lambda y: list(map(lambda x: int(x), y)), list(map(lambda x: x.split(), data))))
safe_reports = 0

for line in data:

    if is_safe_line(line):
        safe_reports += 1
        continue
    
    for i in range(len(line)):
        modified_line = line[:i] + line[i+1:]
        
        if is_safe_line(modified_line):
            safe_reports += 1
            break

print(safe_reports)