# Date Created: 2021-11-09
# Time: 08:47, 12:34
# Author: Brandon Kruger
# Ep 026,027,028

#         01234567801234
parrot = "Norwegian Blue"

# The slice will include up to but not including what you specify in that range.
print(parrot[0:6])  # Norweg
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])
print(parrot[10:14])

print(parrot[10:])

print(parrot[:6] + parrot[6:])

print(parrot[:])

# Mini challenge

letters = "abcdefghijklmnopqrstuvwxyz"

print(letters[0:26])

# First half of letters
print(letters[:13])

# Last half of letters
print(letters[13:])

