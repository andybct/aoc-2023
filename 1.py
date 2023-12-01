from aoc import get_input

data = get_input(1).splitlines()

total = 0
for line in data:
    n = [x for x in line if x.isdigit()]
    total += int(n[0] + n[-1])

print(total)

import re

nums = "one two three four five six seven eight nine".split()
pattern = f"(?=({'|'.join(nums)}|\\d))"

total = 0
for line in data:
    print(line)
    matches = re.findall(pattern, line)
    print(matches)
    num1 = matches[0] if len(matches[0]) == 1 else nums.index(matches[0]) + 1
    num2 = matches[-1] if len(matches[-1]) == 1 else nums.index(matches[-1]) + 1
    total += int(str(num1) + str(num2))

print(total)
    

