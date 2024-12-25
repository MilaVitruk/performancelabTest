import sys

path = sys.argv[1]
with open(path, 'r') as input_file:
    nums = list(map(int, [line.strip() for line in input_file.readlines()]))

average = int(sum(nums)/len(nums))
result = 0
for num in nums:
    delta = abs(average-num)
    result += delta

print(result)

