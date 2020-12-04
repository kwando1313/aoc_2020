my_file = open("day2_1.txt", "r")
content = my_file.readlines()
times = 0

for c in content:
    item = c.split(" ")
    password = item[2]
    letter = item[1].replace(":", "")
    range_list = item[0].split("-")
    low = int(range_list[0])
    high = int(range_list[1])
    if (password[low-1] == (letter) and password[high-1] != letter) or (password[low-1] != (letter) and password[high-1] == letter):
        times = times + 1

print (times)

#print (set(content_list) & set(nl1))
#print (set(nl1) & set(nl2))

# print(content_list)

# find sum = 9
# 1,2,3,4 original list
# 8,7,6,5 nl1
# 4, 2, 0, -2