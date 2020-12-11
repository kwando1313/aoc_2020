my_file = open("day11.txt", "r")
content = my_file.readlines()

seats = []
new_seats = []
unstable = True

for c in content:
    seats.append(c.strip("\n"))

def check_adjacent_seats(x, y, seats):
    filled_seats = 0
    if x != len(seats) - 1 and seats[x+1][y] == "#":
        filled_seats = filled_seats + 1
    if x != len(seats) - 1 and y != len(seats[x]) - 1 and seats[x+1][y+1] == "#":
        filled_seats = filled_seats + 1
    if x != len(seats) - 1 and y != 0 and seats[x+1][y-1] == "#":
        filled_seats = filled_seats + 1
    if y != 0 and seats[x][y-1] == "#":
        filled_seats = filled_seats + 1
    if y != len(seats[x]) - 1 and seats[x][y+1] == "#":
        filled_seats = filled_seats + 1
    if x != 0 and seats[x-1][y] == "#":
        filled_seats = filled_seats + 1
    if x != 0 and y != len(seats[x]) - 1 and seats[x-1][y+1] == "#":
        filled_seats = filled_seats + 1   
    if x != 0 and y != 0 and seats[x-1][y-1] == "#":
        filled_seats = filled_seats + 1   
    return filled_seats

def check_multi_seats_in_row(x, y, seats):
    filled_seats = 0
    for i in range(len(seats)):
        #print x-i
        if (x-i >= 0):
            if i == 0:
                continue
            elif seats[x-i][y] == "#":
                filled_seats = filled_seats + 1
                # print "FOUND A SEAT 1"
                break
            elif seats[x-i][y] == "L":
                break
        else:
            break
    for i in range(len(seats)):
        if (x + i <= len(seats) - 1):
            if i == 0:
                continue
            elif seats[x+i][y] == "#":
                filled_seats = filled_seats + 1
                # print "FOUND A SEAT 2"
                break
            elif seats[x+i][y] == "L":
                break
        else:
            break
    for i in range(len(seats[x])):
        if (y - i >= 0):
            if i == 0:
                continue
            elif seats[x][y-i] == "#":
                filled_seats = filled_seats + 1
                # print "FOUND A SEAT 3"
                break
            elif seats[x][y-i] == "L":
                break         
        else: 
            break  
    for i in range(len(seats[x])):
        if (y + i <= len(seats[x]) - 1):
            if i == 0:
                continue
            elif seats[x][y+i] == "#":
                filled_seats = filled_seats + 1
                # print "FOUND A SEAT 4"
                break
            elif seats[x][y+i] == "L":
                break 
        else:
            break
    for i in range(len(seats)):
        if x-i >= 0 and y-i >= 0:
            if i == 0:
                continue
            elif seats[x-i][y-i] == "#":
                filled_seats = filled_seats + 1
                # print "FOUND A SEAT 5"
                break
            elif seats[x-i][y-i] == "L":
                break
        else:
            break
    for i in range(len(seats)):
        if x+i <= len(seats) - 1 and y+i <= len(seats[x]) - 1:
            if i == 0:
                continue
            elif seats[x+i][y+i] == "#":
                filled_seats = filled_seats + 1
                # print "FOUND A SEAT 6"
                break
            elif seats[x+i][y+i]  == "L":
                break
        else:
            break
    for i in range(len(seats)):
        if x+i <= len(seats) - 1 and y-i >= 0:
            if i == 0:
                continue
            elif seats[x+i][y-i] == "#":
                filled_seats = filled_seats + 1
                # print "FOUND A SEAT 7"
                break
            elif seats[x+i][y-i]  == "L":
                break
        else:
            break
    for i in range(len(seats)):
        if x-i >= 0 and y+i <= len(seats[x]) - 1:
            if i == 0:
                continue
            elif seats[x-i][y+i] == "#":
                filled_seats = filled_seats + 1
                # print "FOUND A SEAT 8"
                break
            elif seats[x-i][y+i]  == "L":
                break
        else:
            break
    # print "There are " + str(filled_seats) + " filled seats that can be seen from " + str(x) + ", " + str(y)
    return filled_seats

while unstable:
    for i in range(len(seats)):
        seat_str = ""
        for j in range(len(seats[i])):
           # print i, j
            if seats[i][j] == "L" and check_multi_seats_in_row(i, j, seats) == 0:
                #print "IMPORTANT" + str(check_multi_seats_in_row(i, j, seats))
                seat_str = seat_str + "#"
            elif seats[i][j] == "#" and check_multi_seats_in_row(i, j, seats) >= 5:
                seat_str = seat_str + "L"
            else:
                seat_str = seat_str + seats[i][j]
        new_seats.append(seat_str)
    if seats == new_seats:
        unstable = False
    else:
        seats = new_seats
        # for seat in seats:
        #     print seat
        # print "-----------------"
        new_seats = []

num_of_occupied = 0
for seat in seats:
    print seat
    num_of_occupied = num_of_occupied + seat.count("#")

print num_of_occupied