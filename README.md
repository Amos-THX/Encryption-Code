# Encryption-Code
This code creates a simple encryption and decryption code using the same encryption key. The key will allow the same characters to be input, i.e. AAAA55555 is a valid encryption key.

A simple algorithm is created by taking each letter of the secret key, removing the letter and appending to the end of the full character list, and then shifting the entire list based on the number of characters in the secret key. This is done to generate the initial cipher characters.

After which, during the encoding/decoding process, the full character list is shifted based on the number of characters in the secret key, so as to jumble up the letters. 

This will achieve the following advantages:
1) Unable to guess the word format through encrypted text. Whitespaces, full stops and punctuation may appear as any other character.
2) There is a possibility for the encrypted character to be the exact same letter as the original character letter.
3) The same character in the actual text will appear as different characters in the encrypted text. i.e. Using secret key "YUiqomdd831$(!lP", the actual text "AAAAA" will become "}d8HW".
