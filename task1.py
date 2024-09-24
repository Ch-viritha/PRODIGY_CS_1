def main():
    plain = input("Enter plaintext: ")
    key = int(input("Enter key value: "))

    print("\n\n\nPlain text:", plain)
    print("\n\nEncrypted text: ", end="")

    cipher = []
    for char in plain:
        if char.isupper():
            cipher_char = chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
        elif char.islower():
            cipher_char = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
        else:
            cipher_char = char
        cipher.append(cipher_char)
        print(cipher_char, end="")

    print("\n\nDecrypted text: ", end="")

    decrypted = []
    for char in cipher:
        if char.isupper():
            plain_char = chr(((ord(char) - ord('A') - key) % 26) + ord('A'))
        elif char.islower():
            plain_char = chr(((ord(char) - ord('a') - key) % 26) + ord('a'))
        else:
            plain_char = char
        decrypted.append(plain_char)
        print(plain_char, end="")

    print()

if __name__ == "__main__":
    main()
