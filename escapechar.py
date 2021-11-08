# Date: 2021-11-08
# Time: 17:45
# Author: Brandon Kruger
# Ep 018,019

# Backslash n, to start a new line.
splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

# Backslash t, to insert a tab.
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')

print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")

# Triple quotes
print("""The pet shop owner said "No, no, \
'e's uh,...he's resting".""")

# Even though its split up you can use backslash to escape it.
anotherSplitString = """This string has been \
split over \
several \
lines"""

print(anotherSplitString)

# 2 methods to escape backslashes, in this example we are printing a path.
print("C:\\Users\\YourUsernameHere\\Desktop\\notes.txt")
print(r"C:\Users\YourUsernameHere\Desktop\notes.txt")
