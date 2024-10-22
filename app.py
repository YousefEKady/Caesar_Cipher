import pyperclip

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
    # Enter Your Message
    message = input("Enter Your Message (or type 'exit' to quit): ").upper()
    
    if message == "EXIT":
        print("Exiting the program...")
        break
    
    # Enter a Key
    key = int(input("Enter Your Key (1 to 25): "))
    
    # Encryption or Decryption
    mode = input("Encryption or Decryption? (e/d): ").lower()
    
    translated = ""  # Encrypted or Decrypted Message
    
    for symbol in message:
        if symbol in letters:
            num = letters.find(symbol)  # Get the number of symbol
            if mode in ["e", "encryption"]:  # Correct check for encryption
                num = num + key
            elif mode in ["d", "decryption"]:  # Correct check for decryption
                num = num - key

            # Handle wraparound
            if num >= len(letters):
                num = num - len(letters)
            elif num < 0:
                num = num + len(letters)

            translated = translated + letters[num]  # Add the correct translated letter
        else:
            translated = translated + symbol  # Non-letter characters remain unchanged
    
    # Output the result
    print(f"Translated message: {translated}")
    pyperclip.copy(translated)
