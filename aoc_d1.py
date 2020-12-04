my_file = open("day1_1.txt", "r")
content = my_file.read()
content_list = content.split("\n")
nl1 = []
nl2 = []
for c in content_list:
    nl1.append(str(2020 - int(c)))

for a in range (len(content_list) - 1):
    for b in range (a + 1, len(content_list)):
        if str(int(content_list[a]) + int(content_list[b])) in nl1:
            print (content_list[a], content_list[b])

#print (set(content_list) & set(nl1))
#print (set(nl1) & set(nl2))

# print(content_list)

# find sum = 9
# 1,2,3,4 original list
# 8,7,6,5 nl1
# 4, 2, 0, -2