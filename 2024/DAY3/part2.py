import re


with open('data') as f: lines = [line.rstrip() for line in f]


def find_pairs(line):
    sum = 0
    list = re.findall("mul\((\d+,\d+)\)", line)
    for pair in list:
        i_pair = [int(a) for a in pair.split(",")]
        sum += i_pair[0] * i_pair[1]
    return sum


mul_result = 0
instructions = ""
for line in lines: instructions += line


blocks = instructions.split("don't()")


mul_result += find_pairs(blocks[0])


for instruction in range(1, len(blocks)):
    do = blocks[instruction].find('do()')
    do_instructions = blocks[instruction][do:]
    mul_result += find_pairs(do_instructions)


print(f"result: {mul_result}")