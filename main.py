MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def get_letter(letter):
    for key, value in MORSE_CODE_DICT.items():
        if value == letter:
            return key


def encrypt(message):
    morse_code_word = ""
    for letter in message:
        if letter != " ":
            morse_code_word += MORSE_CODE_DICT[letter] + " "
        else:
            morse_code_word += " "
    return morse_code_word


def decrypt(message):
    text_word = ""
    # "- . ... -"
    for word in message:
        word_to_letter = word.split(" ")
        for morse_letter in word_to_letter:
            if morse_letter == " ":
                text_word += " "
            else:
                text_word += get_letter(morse_letter)
        text_word += " "
    return text_word


def main():
    print("\nWelcome to Morse Code decryption and encryption program.")
    still_working = True
    while still_working:
        print("\n############################################\n")

        fun = input('For encrypting to Morse Code type "1"\n'
                    'For decrypting to text type "2"\n'
                    'For EXIT from program type "0"\n'
                    'Your choice: ')
        print("\n############################################\n")
        if fun == "1":
            text_to_convert = input("Enter text which you want to encrypt to Morse Code: ").upper()
            result = encrypt(text_to_convert)
            try:
                print(f"Sentence: {text_to_convert} converted to: {result}")
            except KeyError:
                print(
                    "The word or phrase you've provided contains invalid characters"
                    " - we can only convert the letters A-Z, numbers, and spaces to Morse Code in this program.")

        elif fun == "2":
            text_in_morse = input(str("Enter text which you want to decrypt to text: "))
            text_to_decrypt = text_in_morse.strip().split("  ")
            # print(text_to_decrypt)
            encrypted = decrypt(text_to_decrypt)
            # print(encrypted)
            print(f"Sentence: {text_in_morse} converted to: {encrypted}\n")

        elif fun == "0":
            print("Exiting... :)")
            still_working = False
        else:
            print("Wrong key, try again.")


if __name__ == "__main__":
    main()


#
# print(text_word)


