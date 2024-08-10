# Encryption / Decryption code for upper/lower case letters, punctuations, digits & whitespace.
# Requires same encryption key on both ends to encrypt/decrpyt.

import time
import string

#Secret key can include upper and lower case letters, digits, whitespace, multiple times.
secret_key = input('Input encryption key: ')

def get_secret_chars(secret_key):

#Create secret list to be used to jumble up character list
    secret_list = [x for x in secret_key]

    chars = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation + ' '
    chars = list(chars)
    secret_chars = list(chars)

    for letter in secret_list:

        #First remove the letter from chars
        secret_chars.remove(letter)

        #Append character to end of chars
        secret_chars.append(letter)

        #Shuffle chars list by moving based on length of secret key
        secret_chars = secret_chars[len(secret_key)-1:] + secret_chars[:len(secret_key)-1]

    return chars, secret_chars


chars, secret_chars = get_secret_chars(secret_key)

#Now encrypt actual message based on encryption key

actual_text = input("Actual Message: ")
cipher_text = ''

#Replace letters one by one into cipher text.

for letter in actual_text:

    # if letter not in list i.e.is special character, just return same character
    if letter not in chars:
        cipher_text += letter

    else:
    #Find index in initial chars list, then find in secret chars list
        letter_pos = chars.index(letter)

        new_char = secret_chars[letter_pos]

        cipher_text += new_char

    #Also move the secret chars list here so that no 2 letters return the same letter.
    secret_chars = secret_chars[len(secret_key)-1:] + secret_chars[:len(secret_key)-1]

print("Encrypted Text: ",cipher_text)

#Now decipher text. Re-ask for secret key again.

#Secret key can include upper and lower case letters, digits, whitespace, multiple times.
secret_key = input('Input encryption key: ')

chars, secret_chars = get_secret_chars(secret_key)

#Now encrypt actual message based on encryption key

cipher_text = input("Cipher Message: ")
actual_text = ''

#Replace letters one by one into cipher text.

for letter in cipher_text:

    # if letter not in list i.e.is special character, just return same character
    if letter not in secret_chars:
        actual_text += letter

    else:
    #Find index in initial chars list, then find in secret chars list
        letter_pos = secret_chars.index(letter)

        new_char = chars[letter_pos]

        actual_text += new_char

    secret_chars = secret_chars[len(secret_key)-1:] + secret_chars[:len(secret_key)-1]

print("Decrypted Text: " ,actual_text)
