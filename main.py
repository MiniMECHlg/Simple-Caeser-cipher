#Simple Caeser cipher based on spec for AQA
#Made by Jay Gardener(MiniMECH)

"""
The program must
1. Give the user the option to encrypt, decrypt or exit
2. Encrypt - allow the user to enter the plaintext and the shift and then display the ciphertext
3. Decrypt - allow the user to enter the cipher text and the shift and then display the plaintext
4. Exit - stop the program
5. Use sensible variable/function names, have comments and be formatted correctly

It could also
1. Change the ciphertext so that it removes punctuation and put it in blocks of 5 characters
2. Create a brute force decryption algorithm using the attached list of 1000 most common English words
(or using frequency analysis)
"""

"""
Ascii characters
A-Z = 65-90
a-z = 97-122
Space is 32
I would like this to support both upper and lower case characters and numbers
if Z has to go up one it will go to a lower case a instead of an upper case A
"""


# ----------Basic parts for advnaced encryption----------- #


#Splits a word into a list of single characters
def split(word):
    return [char for char in word] 

#Joins a list into a whole string
def join(wordList):
    word = ""
    for char in range (len(wordList)):
        word += wordList[char]
    return word


# -----------------Section for encryption----------------- #


def simple_shift(shiftText, shiftNum):
    encryptedText = ""
    for char in range(len(shiftText)):
        if (ord(shiftText[char]) >= 65 and ord(shiftText[char]) <= 90):
            letterValue = ord(shiftText[char])
            letterValue -= 64 #This gets A to 1 this means we can tell which value this should be
            newValue = letterValue + shiftNum

            div = newValue//26
            newValue = newValue%26

            if newValue == 0:
                newValue += 90
            elif div%2 == 0: #if it is even it needs to be a cap
                newValue += 64
            else: #if odd it needs to be a lowercase
                newValue += 96

            encryptedText += chr(newValue)

        elif (ord(shiftText[char]) >= 97 and ord(shiftText[char]) <= 122):
            letterValue = ord(shiftText[char])
            letterValue -= 96  # This gets A to 1 this means we can tell which value this should be
            newValue = letterValue + shiftNum

            div = newValue//26
            newValue = newValue%26
            
            if newValue == 0:
                newValue += 122
            elif div%2 == 1: #if it is odd it needs to be a cap
                newValue += 64
            else: #if even it has to be a lower case
                newValue += 96

            encryptedText += chr(newValue)

        else:
            encryptedText += shiftText[char]

    return encryptedText


def advanced_shift(shiftText, shiftNum):
    encyptedText = ""
    char = 0
    while char != (len(shiftText)):
        if (char % 5) == 0 and (char != 0):
            textArray = split(shiftText)
            textArray.insert(char, " ")
            shiftText = join(textArray)

        elif((ord(shiftText[char]) != 32) and not ((ord(shiftText[char]) >= 65 and ord(shiftText[char]) <= 90) or (ord(shiftText[char]) >= 97 and ord(shiftText[char]) <= 122))):
            textArray = split(shiftText)
            del textArray[char]
            shiftText = join(textArray)

        if (ord(shiftText[char]) >= 65 and ord(shiftText[char]) <= 90):
            caps = True
            letterValue = ord(shiftText[char])
            letterValue -= 64 #This gets A to 1 this means we can tell which value this should be
            newValue = letterValue + shiftNum

            div = newValue//26
            newValue = newValue%26

            if newValue == 0:
                newValue += 90
            elif div%2 == 0: #if it is even it needs to be a cap
                newValue += 64
            else: #if odd it needs to be a lowercase
                newValue += 96

            encyptedText += chr(newValue)

        elif (ord(shiftText[char]) >= 97 and ord(shiftText[char]) <= 122):
            caps = False
            letterValue = ord(shiftText[char])
            letterValue -= 96  # This gets A to 1 this means we can tell which value this should be
            newValue = letterValue + shiftNum

            div = newValue//26
            newValue = newValue%26

            if newValue == 0:
                newValue += 122
            elif div%2 == 1: #if it is odd it needs to be a cap
                newValue += 64
            else: #if even it has to be a lower case
                newValue += 96

            encyptedText += chr(newValue)

        else:
            encyptedText += shiftText[char]
        char += 1

    return encyptedText
        


def encyption():
    plainText = input("What do you want to encrypt\n")
    while True:
        try:
            shift = int(input("What do you want the shift to be: "))
            break
        except:
            print("Please enter an integer number\n")
            continue
    print("\nPlease pick an option\n")
    print("Would you like a\n1.Simple Shift\n2.Advanced shift")
    while True:
        try:
            shiftOption = int(input(":>>"))
        except:
            print("Please enter an integer number\n")
            continue
        finally:
            if (shiftOption == 1):
                encryptedText = simple_shift(plainText, shift)
                break
            elif (shiftOption == 2):
                encryptedText = advanced_shift(plainText, shift)
                break
            else:
                print("\nPlease enter a number between 1 and 2\n")
                continue
    print(encryptedText)


# -----------------Section for Decryption----------------- #


def simple_decryption(textToDecrypt):
    while True:
        try:
            shiftNum = int(input("What would you like to shift this by to decrypt it: "))
            break
        except:
            print("Please enter an integer number")
            continue
    decryptedText = ""
    caps = False
    for char in range(len(textToDecrypt)):
        if (ord(textToDecrypt[char]) >= 65 and ord(textToDecrypt[char]) <= 90):
            caps = True
            letterValue = ord(textToDecrypt[char])
            letterValue -= 64 #This gets A to 1 this means we can tell which value this should be
            newValue = letterValue + shiftN2um

            while newValue > 26:
                newValue -= 26
                caps = not caps

            while newValue < 1:
                newValue += 26
                caps = not caps

            if caps == True:
                newValue += 64
            else:
                newValue += 96

            decryptedText += chr(newValue)

        elif (ord(textToDecrypt[char]) >= 97 and ord(textToDecrypt[char]) <= 122):
            caps = False
            letterValue = ord(textToDecrypt[char])
            letterValue -= 96  # This gets A to 1 this means we can tell which value this should be
            newValue = letterValue + shiftNum

            while newValue > 26:
                newValue -= 26
                caps = not caps

            while newValue < 1:
                newValue += 26
                caps = not caps

            if caps == True:
                newValue += 64
            else:
                newValue += 96

            decryptedText += chr(newValue)

        else:
            decryptedText += shiftText[char]

    return decryptedText
    


def advanced_decryption(textToDecrypt):
    pass


def decryption():
    plainText = input("What text would you like to decrypt\n")
    while True:
        try:
            print("Please pick an option\n")
            print("Would you like a\n1. Set shift decryption\n 2. Automatic shift")
            decryptionOption = int(input(">>:"))
        except:
            print("\nPlease enter an integer number!")
            continue
        finally:
            if (decryptionOption == 1):
                decryptedText = simple_decryption(plainText)
                break
            elif (decryptionOption == 2):
                decryptedText = advanced_decryption(plainText)
                break
            else:
                print("\nPlease enter a number between 1 and 2\n")
                continue
    print(decryptedText)


# ------------Things that happen at the start------------- #


def start():
    while True:
        print("What would you like to do: ")
        print("1. Encypt")
        print("2. Decrypt")
        print("3. Exit")
        try:
            option = int(input("What would you like to do: "))
        except:
            print("Please make sure to enter a number value!\n")
            continue

        if(option == 1):
            encyption()
        elif(option == 2):
            decryption()
        elif(option == 3):
            quit()
        else:
            print("Please enter a value between 1 and 3\n")
            continue

start()