my_file = open("day8.txt", "r")
content = my_file.readlines()

sum = 0
i = 0
commands = []
full_commands = []
# #MakeMyBag

for c in content:
    full_commands.append(c.strip("\n"))

while i < range(len(full_commands)):
    full_string = full_commands[i].strip("\n")
    op = full_string.split(" ")[0]
    value = int(full_string.split(" ")[1])
    if i in commands:
        #print "INFINITE LOOP"
        #print sorted(commands)
        break
    else:
        commands.append(i)
   # print "op: " + op + str(value)
    if op == "acc":
        sum = sum + value
        i = i + 1
    elif op == "jmp":
        #print "Jump: " + str(value)
        i = i + value
    else:
        i = i + 1
   # print "i: " + str(i)

sum = 0
i = 0
#commands = []
escape = True
loop_commands = []

for fix_command in commands:
    sum = 0
    escape = True
    loop_commands = []
    i = 0
    print fix_command
    #print len(full_commands)
    while i <= range(len(full_commands) - 1):
        if i > len(full_commands) - 1:
            break
        full_string = full_commands[i].strip("\n")
        op = full_string.split(" ")[0]
        value = int(full_string.split(" ")[1])
        if i in loop_commands:
            #print "INFINITE LOOP"
            #print sorted(commands)
            escape = False
            print "Hi"
            break
        else:
            loop_commands.append(i)
        if full_commands[fix_command].strip("\n").split(" ")[0] == "jmp" and i == fix_command:
            op = "nop"
           # print "SWAPPED"
        if full_commands[fix_command].strip("\n").split(" ")[0] == "nop" and i == fix_command:
            op = "jmp"
           # print "SWAPPED"
        if op == "acc":
            sum = sum + value
            i = i + 1
        elif op == "jmp":
            #print "Jump: " + str(value)
            i = i + value
        else:
            i = i + 1
    
    if escape:
        print "Escaped"
        print sum

print sum