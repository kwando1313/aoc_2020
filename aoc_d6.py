my_file = open("day6.txt", "r")
content = my_file.readlines()

questions = 0
blank_set = set()

## Anyone
for c in content:
    if c != "\n":
        for letter in c.strip("\n"):
            blank_set.add(letter)
    else:
        #print blank_set
        questions = questions + len(blank_set)
        blank_set = set()

## Everyone
blank_list = []
passengers = 0
questions = 0
for c in content:
    if c != "\n":
        for letter in c.strip("\n"):
            blank_list.append(letter)
        passengers = passengers + 1
    else:
        for x in set(blank_list):
            if blank_list.count(x) == passengers:
                questions = questions + 1
        blank_list = []
        passengers = 0

print questions