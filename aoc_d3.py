my_file = open("day3_1.txt", "r")
content = my_file.readlines()
x_axis = 0
trees_1 = 0 #+1
trees_2 = 0 #+3
trees_3 = 0 #+5
trees_4 = 0 #+7
trees_5 = 0

mod_value = 31

for c in content:
    mod_value = 31
    if c[x_axis % mod_value] == "#":
      #  print c
        trees_1 = trees_1 + 1
    x_axis = x_axis + 1

#+3
x_axis = 0

for c in content:
    mod_value = 31
    if c[x_axis % mod_value] == "#":
      #  print c
        trees_2 = trees_2 + 1
    x_axis = x_axis + 3

#+5
x_axis = 0

for c in content:
    mod_value = 31
    if c[x_axis % mod_value] == "#":
      #  print c
        trees_3 = trees_3 + 1
    x_axis = x_axis + 5

#+7
x_axis = 0

for c in content:
    mod_value = 31
    if c[x_axis % mod_value] == "#":
       # print c
        trees_4 = trees_4 + 1
    x_axis = x_axis + 7

x_axis = 0
for c in content[::2]:
    mod_value = 31
    if c[x_axis % mod_value] == "#":
       # print c
        trees_5 = trees_5 + 1
    x_axis = x_axis + 1

print (trees_1, trees_2, trees_3, trees_4, trees_5)
print (trees_1 * trees_2 * trees_3 * trees_4 * trees_5)

#print (set(content_list) & set(nl1))
#print (set(nl1) & set(nl2))

# print(content_list)

# find sum = 9
# 1,2,3,4 original list
# 8,7,6,5 nl1
# 4, 2, 0, -2