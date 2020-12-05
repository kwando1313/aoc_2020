import math

def half_divide(boarding_pass, lower_range, upper_range):
    half = boarding_pass[0]
    #print half
    if upper_range - lower_range > 1:
        #print lower_range, upper_range
        if half == "L" or half == "F":
            upper_range = int(math.floor((lower_range + upper_range) / 2))
            #print "Range: " + str(lower_range) + "-" + str(upper_range)
            return half_divide (boarding_pass[1:], int(lower_range), upper_range)
        if half == "R" or half == "B":
            lower_range = int(math.ceil((lower_range + upper_range) / 2)) + 1
            #print "Range: " + str(lower_range) + "-" + str(upper_range)
            return half_divide (boarding_pass[1:], lower_range, int(upper_range))
    else:
        #print lower_range, upper_range
        if half == "L" or half == "F":
            return lower_range
        if half == "R" or half == "B":
            return upper_range 

my_file = open("day5.txt", "r")
content = my_file.readlines()
ids = []
highest_id = 0

for c in content:
    boarding_pass = c.strip("\n")
    row = int(half_divide(boarding_pass[:-3], 0, 127))
    #print row
    column = int(half_divide(boarding_pass[-3:], 0, 7))
   # print column
    current_id = (row * 8 + column)
    ids.append(current_id)
    if highest_id < current_id:
        highest_id = current_id

print sorted(ids)