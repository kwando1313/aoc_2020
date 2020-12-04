import re

my_file = open("day4_1.txt", "r")
content = my_file.readlines()
prev_valid = 0
valid_passports = 0
total_passports = 0
current_passport = {}
eye_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

for c in content:

    if c != "\n":
        passport_line = c.split(" ")
        temp_map = dict(map(str.strip, line.split(':', 1)) for line in passport_line)
        current_passport.update(temp_map)
    else:
        total_passports = total_passports + 1
        if "byr" in current_passport and "iyr" in current_passport and "eyr" in current_passport and "hgt" in current_passport and "hcl" in current_passport and "ecl" in current_passport and "pid" in current_passport:
            prev_valid = prev_valid + 1
            if int(current_passport["byr"]) >= 1920 and int(current_passport["byr"]) <= 2002:
                if int(current_passport["iyr"]) >= 2010 and int(current_passport["iyr"]) <= 2020:
                    if int(current_passport["eyr"]) >= 2020 and int(current_passport["eyr"]) <= 2030:
                        if ( "cm" in current_passport["hgt"] and (int(current_passport["hgt"][:-2]) >= 150 and int(current_passport["hgt"][:-2]) <=193) ) or ("in" in current_passport["hgt"] and (int(current_passport["hgt"][:-2]) >= 59 and int(current_passport["hgt"][:-2]) <=76) ):
                            if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', current_passport["hcl"]):
                                if current_passport["ecl"] in eye_colours:
                                    if len(current_passport["pid"]) == 9:
                                        print ("VALID: " + str(current_passport))
                                        valid_passports = valid_passports + 1
                                    else:
                                        print ("INVALID PID: " + current_passport["pid"])
                                else:
                                    print ("INVALID EYE COLOR: " + current_passport["ecl"])
                            else:
                                print ("INVALID HAIR COLOR: " + current_passport["hcl"])
                        else: 
                            print ("INVALID HEIGHT: " + current_passport["hgt"])
                    else: 
                        print ("INVALID EXPIRY YEAR: " + current_passport["eyr"])
                else:
                    print ("INVALID ISSUE YEAR: " + current_passport["iyr"])
            else:
                print ("INVALID BIRTH YEAR: " + current_passport["byr"])
        #print current_passport
        current_passport = {}
print prev_valid
print valid_passports
print total_passports