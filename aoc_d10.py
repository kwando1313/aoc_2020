my_file = open("day10.txt", "r")
content = my_file.readlines()

voltages = []
sorted_voltages = []
one_away = 0
three_away = 0
trib = [1, 1, 2, 4, 7, 13]

for c in content:
    voltages.append(int(c.strip("\n")))

sorted_voltages = sorted(voltages)

print sorted_voltages

i = 0
j = 0
value = 1

while i < len(sorted_voltages):
    if i+1 < len(sorted_voltages) and sorted_voltages[i+1] - sorted_voltages[i] == 1:
        #print "Voltage: " + str(sorted_voltages[i])
        one_away = one_away + 1
    else:
        three_away = three_away + 1
        value = value * trib[(i - j)]
        #print value
        j = i + 1
    i = i + 1

print one_away
print three_away
print one_away * three_away
print value # Tribonacci numbers. I don't want to write code to re-find this answer.
#
#1,3,2,1,1,2,1,1,1,1