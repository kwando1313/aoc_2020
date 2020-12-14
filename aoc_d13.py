import math

my_file = open("day13.txt", "r")
content = my_file.readlines()

bus_stuff = []
ids = []

for c in content:
    bus_stuff.append(c.strip("\n"))

# Part 1
# start_time = int(bus_stuff[0])

# for id in bus_stuff[1].split(","):
#     if id != "x":
#         ids.append(int(id))

# smallest = 10000000
# bus_id = 0

# for id in ids:
#     if id - (start_time % id) < smallest:
#         smallest = id - (start_time % id)
#         bus_id = id

# print bus_id
# print smallest
# print smallest * bus_id

for id in bus_stuff[1].split(","):
    ids.append(id)

diffs = []
counter = 0
for id in ids:
    if id != "x":
        diffs.append(counter)
    counter = counter + 1
print diffs
print ids

x = 7764462
x = 25029320182775

searching = True

print ((29 * 10419) + 19) % 41
print ((29 * 10419) + 29) % 521
# Smallest should be 31780 ???

# Should be looking for
# x mod 29 = 0, x + 19 mod 41 = 0, x + 29 mod 521 = 0, x + 37 mod 23 = 0, x + 42 mod 13 = 0, x + 46 mod 17 = 0, x + 60 mod 601 = 0
# x + 66 mod 37 = 0, x + 79 mod 19 = 0

while (searching):
    if ((29*x) + 29) % 521 == 0 and ((29*x) + 19) % 41 == 0 and ((29*x) + 37) % 23 == 0 and ((29*x) + 42) % 13 == 0 and ((29*x) + 46) % 17 == 0 and ((29*x) + 60) % 601 == 0 and ((29*x) + 66) % 37 == 0 and ((29*x) + 79) % 19 == 0:
        print x
        searching = False
    x = x + 12837961
print "Hi"
print 25029320182775 * 29