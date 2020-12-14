import math
import itertools

my_file = open("day14.txt", "r")
content = my_file.readlines()

numbers_in_memory = {}
mask = ""

# Part 1
# for c in content:
#     string = c.strip("\n")
#     if string.startswith("mask"):
#         mask = string.strip("mask = ")
#         print mask
#     else:
#         number = int(string.split(" = ")[1])
#         binary_number = bin(number)[2:].zfill(len(mask))
#         memory_location = string.split(" = ")[0].strip("mem[]")
#         new_number = ""
#         i = 0
#         while i < len(mask):
#             if mask[i] != "X":
#                 if mask[i] == "0":
#                     new_number = new_number + "0"
#                 elif mask[i] == "1":
#                     new_number = new_number + "1"
#             else:
#                 new_number = new_number + binary_number[i]
#             i = i + 1
#         numbers_in_memory[memory_location] = int(new_number, 2)

# Part 2
for c in content:
    string = c.strip("\n")
    if string.startswith("mask"):
        mask = string.strip("mask = ")
        #print "Mask: " + mask
    else:
        number = int(string.split(" = ")[1])
        memory_location = int(string.split(" = ")[0].strip("mem[]"))
        binary_number = bin(memory_location)[2:].zfill(len(mask))

        new_number = ""
        i = 0
        while i < len(mask):
            if mask[i] == "X":
                new_number = new_number + "X"
            elif mask[i] == "0":
                new_number = new_number + binary_number[i]
            elif mask[i] == "1":
                new_number = new_number + "1"
            i = i + 1
        # print "Number: " + new_number
        number_of_combinations = new_number.count("X")
        # print number_of_combinations

        # Somehow get all the combinations of binary here to replace the Xs
        li = []
        for i in itertools.product([0,1], repeat=number_of_combinations):
            li.append(''.join(map(str, i)))

        #print li
        for item in li:
            i = 0
            temp_string = ""
            for char in new_number:
                if char == "X":
                    temp_string = temp_string + item[i]
                    i = i + 1
                else:
                    temp_string = temp_string + char
            
            # print "Memory location: " + str(memory_location)
            # print "Binary value: " + temp_string
            # print "Decimal value: " + str(int(temp_string, 2))
            numbers_in_memory[int(temp_string, 2)] = number

        #numbers_in_memory[memory_location] = int(new_number, 2)
#print numbers_in_memory
print sum(numbers_in_memory.itervalues())
