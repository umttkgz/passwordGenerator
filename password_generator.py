import random

def generate_password(length, lower, upper, numbers, symbols):
  """Generates a random password of the specified length, with the specified character requirements.

  Args:
    length: The length of the password to generate.
    lower: Whether to include lowercase letters in the password.
    upper: Whether to include uppercase letters in the password.
    numbers: Whether to include numbers in the password.
    symbols: Whether to include symbols in the password.

  Returns:
    A random password of the specified length, with the specified character requirements.
  """

  characters = ""
  if lower:
    characters += "abcdefghijklmnopqrstuvwxyz"
  if upper:
    characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  if numbers:
    characters += "0123456789"
  if symbols:
    characters += "~!@#$%^&*()_+{}|:\"<>?,./"

  password = ""
  for _ in range(length):
    password += random.choice(characters)

  return password

def main():
  """Prompts the user for the password requirements and generates a random password.
  """

  length = int(input("Enter the length of the password: "))
  lower = input("Include lowercase letters? (y/n): ") == "y"
  upper = input("Include uppercase letters? (y/n): ") == "y"
  numbers = input("Include numbers? (y/n): ") == "y"
  symbols = input("Include symbols? (y/n): ") == "y"
  numOfPasswords = int(input("Number of passwords you want to generate: "))
  
  truthList = []
  if lower == True:
    truthList.append(True)
  else:
    truthList.append(False)
  #print("lower:",lower)

  if upper == True:
    truthList.append(True)
  else:
    truthList.append(False)

  if numbers == True:
    truthList.append(True)
  else:
    truthList.append(False)

  if symbols == True:
    truthList.append(True)
  else:
    truthList.append(False)

  #print("Truthlist:",truthList)
  count = 0

  while count < numOfPasswords:
    list = []
    password = generate_password(length, lower, upper, numbers, symbols)
    list = checkCharacters(lower, upper, numbers, symbols, length, password)
    #print("list:",list)
    if truthList != list:
      continue
    print("Your password is: " + password)
    count += 1

def checkCharacters(lower, upper, numbers, symbols, length, password):
  lowerExist = False
  #print(password)
  if lower == True:
    for i in password:
      if i in "abcdefghijklmnopqrstuvwxyz":
        lowerExist = True
        break
  upperExist = False
  if upper == True:
    for i in password:
      if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        upperExist = True
        break
  numberExist = False
  if numbers == True:
    for i in password:
      if i in "0123456789":
        numberExist = True
        break
  symbolExist = False
  if symbols == True:
    for i in password:
      if i in "~!@#$%^&*()_+{}|:\"<>?,./":
        symbolExist = True
        break
  return [lowerExist, upperExist, numberExist, symbolExist]

  
if __name__ == "__main__":
  main()