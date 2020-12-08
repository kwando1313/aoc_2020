my_file = open("day7.txt", "r")
content = my_file.readlines()

bags = {}
total = 0
nested_bag_colours = []

# def find_bags(color, bags):
#     for colour in bags:
#         if color in bags[colour]:
#             print colour, bags[colour]
#             return find_bags(colour, bags) + 1
#     return 0

## Anyone
for c in content:
    full_string = c.strip("\n")
    main_colour = full_string.split(" bag")[0]
    bag_contains_full = full_string.split("contain ")[1].split(", ")
    colours = []
    if bag_contains_full[0] != "no other bags.":
        for colour in bag_contains_full:
            actual_colour_name = colour.split(" ")[1] + " " + colour.split(" ")[2]
            number = int(colour.split(" ")[0])
            colours.append({actual_colour_name: number})
    bags[main_colour] = colours
#print bags
#print bags
find_bags = []
all_colours = set()

find_bags.append("shiny gold")

#total = find_bags("shiny gold", bags)

# How many bags can contain a shiny gold bag?
while len(find_bags) > 0:
    for colour in bags:
        #print bags[colour]
        if bags[colour]:
            for bag in bags[colour]:
                #print bag
                if find_bags[0] in bag:        
                    if colour not in find_bags and colour not in all_colours:
                        find_bags.append(colour)
                        total = total + 1
                    all_colours.add(colour)
    find_bags.pop(0)

#print total

# How many bags does a shiny gold bag contain?

find_colour = "shiny gold"

def num_bags (bags, find_colour, total):
    if find_colour in bags and bags.get(find_colour):
        for colour in bags.get(find_colour):
            # number of bags = itself + the number of bags within
            total = total + (colour[colour.keys()[0]] * num_bags(bags, colour.keys()[0], 0)) + colour[colour.keys()[0]] 
    return total

total = 0

for colour in bags.get(find_colour):
    total = total + colour[colour.keys()[0]] * num_bags(bags, colour.keys()[0], 0) + colour[colour.keys()[0]] 
  # print "Current total: " + str(total)


print total

