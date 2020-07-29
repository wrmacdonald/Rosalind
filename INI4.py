with open("/Users/wesmacdonald/Downloads/rosalind_ini4.txt") as file:
    nums = file.readline()
    nums_split = nums.split()
a = int(nums_split[0])
b = int(nums_split[1])
odd_nums_sum = 0

for i in range(a, b):
    if i % 2 == 1:
        odd_nums_sum += i
print(f"The sum of all odd numbers between {a} and {b} is: {odd_nums_sum}")