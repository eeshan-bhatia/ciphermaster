def caesar(text, key):
    
    result = ""
 
    for i in range(len(text)):
        letter = text[i]
 
        if (letter.isupper()):
            result += chr((ord(letter) + key-65) % 26 + 65)

        else:
            result += chr((ord(letter) + key - 97) % 26 + 97)

    return result

print("Welcome to CipherMaster. Which cipher would you like to use today?")
chosen_letter = input("Type 'c' for Caesar Cipher : ")

if chosen_letter == "C" or "c":
    string = str(input("Enter text to be encrypted: "))
    shift = int(input("Enter shift key: "))
    print(caesar(string, shift))
        
        
    
    