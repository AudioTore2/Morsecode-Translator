import winsound

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

def to_morse(text):
    morse = ''
    for char in text:
        if char.upper() in morse_code:
            morse += morse_code[char.upper()] + ' '
            winsound.Beep(1000, 200)  # Add beep sound
        else:
            morse += char
    return morse

def to_english(morse):
    english = ''
    morse = morse.split(' ')
    for char in morse:
        for key, value in morse_code.items():
            if char == value:
                english += key
                winsound.Beep(1000, 200)  # Add beep sound
    return english

def main():
    print("Welcome to Morse Code Translator")
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        text = input("Enter the text: ")
        print("Morse Code:", to_morse(text))
    elif choice == 2:
        morse = input("Enter the Morse Code: ")
        print("Text:", to_english(morse))
    else:
        print("Invalid choice")

main()