import re

data = open("data","r").read()

# regex to match valid mul instructions
# allows for potential whitespace and ignores invalid characters
mul_pattern = r'mul\s*\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)'

correct = re.findall(mul_pattern, data)
total_sum = sum(int(num1) * int(num2) for num1, num2 in correct)
    
print(f"result: {total_sum}")