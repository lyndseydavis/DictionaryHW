# Lyndsey Davis -- Dictionary Exercise

################################# PART ONE###########################################
# create course dictionaries
course_room = {
    "CS101": 3004,
    "CS102": 4501,
    "CS103": 6755,
    "NT110": 1244,
    "CM241": 1411,
}
course_instructor = {
    "CS101": "Haynes",
    "CS102": "Alvarado",
    "CS103": "Rich",
    "NT110": "Burke",
    "CM241": "Lee",
}
course_time = {
    "CS101": "8:00 AM",
    "CS102": "9:00 AM",
    "CS103": "10:00 AM",
    "NT110": "11:00 AM",
    "CM241": "1:00 PM",
}
# check dictionaries
"""
print(course_room)
print(type(course_room))
print(course_instructor)
print(type(course_instructor))
print(course_time)
print(type(course_time))
"""
# create input variable for course numnber
course_number = input("Enter Course Number: ")

# find course and dispaly details
if course_number in course_room:
    print("Course #", course_number, "details are below.")
    print("Room location: ", course_room[course_number])
    print("Instructor: ", course_instructor[course_number])
    print("Meeting Time: ", course_time[course_number])
else:
    print("Course Number not found.")

############################################ PART TWO ############################################

codes = {
    "A": "q",
    "a": "w",
    "B": "e",
    "b": "r",
    "C": "t",
    "c": "y",
    "D": "u",
    "d": "i",
    "E": "o",
    "e": "p",
    "F": "a",
    "f": "s",
    "G": "d",
    "g": "f",
    "H": "g",
    "h": "m",
    "I": "j",
    "i": "k",
    "J": "l",
    "j": "z",
    "K": "x",
    "k": "c",
    "L": "v",
    "l": "b",
    "M": "n",
    "m": "h",
    "N": "Q",
    "n": "W",
    "O": "E",
    "o": "R",
    "P": "T",
    "p": "Y",
    "Q": "U",
    "q": "I",
    "R": "O",
    "r": "P",
    "S": "A",
    "s": "1",
    "T": "D",
    "t": "F",
    "U": "G",
    "u": "H",
    "V": "J",
    "v": "K",
    "W": "L",
    "w": "Z",
    "X": "6",
    "x": "C",
    "Y": "V",
    "y": "B",
    "Z": "N",
    "z": "M",
}
# double check length to ensure included all letters
# len(codes)

# open txt file
info_security = open("info_security.txt", "r")
# check file
##print(infosec.readline())
infosec = info_security.read()
info_security.close()
# create encrypted file
encrypt = open("encrypt_info_security.txt", "w")

# read txt file and write to new file
for letter in range(len(infosec)):
    if letter in codes:
        encrypt.write(codes[letter])
    else:
        print(letter)


encrypt.close()
