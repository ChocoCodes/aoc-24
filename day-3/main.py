import re

with open('data/input.txt') as f:
    line = f.read().strip()

# Task 1
valid_ins = re.findall(r"mul\((\d+),(\d+)\)", line)
match_ints = [tuple(map(int, ins)) for ins in valid_ins]

ans = 0
ans = ans + sum([a * b for a, b in match_ints])
print(f"Task 1: {ans}")

valid_ins_t2 = re.findall(r"(?:mul\((\d+),(\d+)\))|(do\(\)|don't\(\))", line)
ans_t2 = 0
do_ins = True
# Task 2
for ins in valid_ins_t2:
    if do_ins and ins[2] == "":
        ans_t2 += int(ins[0]) * int(ins[1])
    else:
        do_ins = True if ins[2] == "do()" else False
print(f"Task 2: {ans_t2}")