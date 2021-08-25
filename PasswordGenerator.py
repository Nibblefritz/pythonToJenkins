import random

#Welcome
print("Welcom to the password genie")
#Ask how many letters in the password
letterCount = int(input("How many letters would you like in the password? "))
#Ask how many symbols in the password
symbolCount = int(input("How many symbols? "))
#Ask how many numbers
numberCount = int(input("How many numbers? "))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '?', '~', '+', '=', '-', '_']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

passwordList = []

#Easy mode
for char in range(1, letterCount+1):
    randomChar = random.choice(letters)
    passwordList.append(randomChar)

for char in range(1, symbolCount+1):
    randomChar = random.choice(symbols)
    passwordList.append(randomChar)

for char in range(1, numberCount+1):
    randomChar = random.choice(numbers)
    passwordList.append(randomChar)

password = ""

#Easy password
for char in passwordList:
    password+=char;

print(f"Your password is: {password}")

#Hard password (scramble it)
random.shuffle(passwordList)
hardPassword = ''.join(passwordList)
print(f"Your scrambled password is: {hardPassword}")