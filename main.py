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

# -----------------Section for encryption----------------- #

def simple_shift(shift_text, shift_num):
    encyptedText = ""
    caps = False
    for char in range(len(shift_text)):
        if (ord(shift_text[char]) >= 65 and ord(shift_text[char]) <= 90):
            caps = True
            letter_value = ord(shift_text[char])
            letter_value -= 64 #This gets A to 1 this means we can tell which value this should be
            new_value = letter_value + shift_num

            while new_value > 26:
                new_value -= 26
                caps = not caps

            while new_value < 1:
                new_value += 26
                caps = not caps

            if caps == True:
                new_value += 64
            else:
                new_value += 96

            encyptedText += chr(new_value)

        elif (ord(shift_text[char]) >= 97 and ord(shift_text[char]) <= 122):
            caps = False
            letter_value = ord(shift_text[char])
            letter_value -= 96  # This gets A to 1 this means we can tell which value this should be
            new_value = letter_value + shift_num

            while new_value > 26:
                new_value -= 26
                caps = not caps

            while new_value < 1:
                new_value += 26
                caps = not caps

            if caps == True:
                new_value += 64
            else:
                new_value += 96

            encyptedText += chr(new_value)

        else:
            encyptedText += shift_text[char]

    return encyptedText


def advanced_shift(shift_text, shift_num):
    pass


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
            letter_value = ord(textToDecrypt[char])
            letter_value -= 64 #This gets A to 1 this means we can tell which value this should be
            new_value = letter_value + shiftN2um

            while new_value > 26:
                new_value -= 26
                caps = not caps

            while new_value < 1:
                new_value += 26
                caps = not caps

            if caps == True:
                new_value += 64
            else:
                new_value += 96

            decryptedText += chr(new_value)

        elif (ord(textToDecrypt[char]) >= 97 and ord(textToDecrypt[char]) <= 122):
            caps = False
            letter_value = ord(textToDecrypt[char])
            letter_value -= 96  # This gets A to 1 this means we can tell which value this should be
            new_value = letter_value + shiftNum

            while new_value > 26:
                new_value -= 26
                caps = not caps

            while new_value < 1:
                new_value += 26
                caps = not caps

            if caps == True:
                new_value += 64
            else:
                new_value += 96

            decryptedText += chr(new_value)

        else:
            decryptedText += shift_text[char]

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