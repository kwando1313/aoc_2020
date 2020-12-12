import math

my_file = open("day12.txt", "r")
content = my_file.readlines()

instructions = []
position = [0, 0]
directions = ["E", "S", "W", "N"]
current_direction = "E"

for c in content:
    instructions.append(c.strip("\n"))

# Part 1
# for instruction in instructions:
#     amount = int(instruction[1:])
#     if instruction.startswith("N"):
#         position[0] += amount
#     if instruction.startswith("S"):
#         position[0] -= amount
#     if instruction.startswith("E"):
#         position[1] += amount
#     if instruction.startswith("W"):
#         position[1] -= amount
#     if instruction.startswith("L"):
#         current_direction = directions[((directions.index(current_direction) - (amount / 90)) + 4) % 4]
#     if instruction.startswith("R"):
#         current_direction = directions[(directions.index(current_direction) + (amount / 90)) % 4]
#     if instruction.startswith("F"):
#         if current_direction == "N":
#             position[0] += amount
#         if current_direction == "S":
#             position[0] -= amount
#         if current_direction == "E":
#             position[1] += amount
#         if current_direction == "W":
#             position[1] -= amount
# print position

# Part 2
waypoint = [1, 10]

for instruction in instructions:
    amount = int(instruction[1:])
    if instruction.startswith("N"):
        waypoint[0] += amount
    if instruction.startswith("S"):
        waypoint[0] -= amount
    if instruction.startswith("E"):
        waypoint[1] += amount
    if instruction.startswith("W"):
        waypoint[1] -= amount
    if instruction.startswith("L"):
        new_waypoint_x = waypoint[0] * math.cos(math.radians(-amount)) - waypoint[1] * math.sin(math.radians(-amount))
        new_waypoint_y = waypoint[1] * math.cos(math.radians(-amount)) + waypoint[0] * math.sin(math.radians(-amount))
        waypoint[0] = new_waypoint_x
        waypoint[1] = new_waypoint_y
    if instruction.startswith("R"):
        new_waypoint_x = waypoint[0] * math.cos(math.radians(amount)) - waypoint[1] * math.sin(math.radians(amount))
        new_waypoint_y = waypoint[1] * math.cos(math.radians(amount)) + waypoint[0] * math.sin(math.radians(amount))
        waypoint[0] = new_waypoint_x
        waypoint[1] = new_waypoint_y
    if instruction.startswith("F"):
        position[0] += amount * waypoint[0]
        position[1] += amount * waypoint[1]
print position