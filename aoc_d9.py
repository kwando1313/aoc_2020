my_file = open("day9.txt", "r")
content = my_file.readlines()

previous = 5
full_numbers = []
range_numbers = []
invalid_number = 0
# #MakeMyBag

for c in content:
    full_numbers.append(int(c.strip("\n")))

range_numbers = full_numbers[0:25]
#print full_numbers

# Part one
i = 25
while i < len(full_numbers):
    valid = False
    for num in range_numbers:
        if (full_numbers[i] - num) in range_numbers:
            valid = True
    if not valid:
        invalid_number = full_numbers[i]
        break
    valid = False
   # print range_numbers
    range_numbers.pop(0)
    range_numbers.append(full_numbers[i])
    i = i + 1

print invalid_number

# Part two
sum_to_find = 393911906

i = 100
j = 100


# while i < len(full_numbers):
#     test_sum = 0

#     while test_sum < sum_to_find:
#         test_sum = test_sum + full_numbers[j]
#         j = j + 1
#         if test_sum == sum_to_find:
#             print i, j
#     i = i + 1
#     j = i

file2 = open("day9_subset.txt")
content = file2.readlines()

full_numbers = []

for c in content:
    full_numbers.append(int(c.strip("\n")))

print sorted(full_numbers)