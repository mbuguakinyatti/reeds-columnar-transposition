# Transposition cipher encryption
def main():
    message = input('Enter message: ').replace(' ', '#')  # Replace spaces with #
    print('This is the message to be encrypted: ' + message)
    custom_key = [2, 4, 0, 1, 3, 7, 5, 6]  # Define your custom key
    key = len(custom_key)  # Key is the length of the custom key
    print('This is the Key:', custom_key)
    cipher_text = transposeEncrypt(custom_key, message)
    print('This is the cipher text: ' + cipher_text)

def transposeEncrypt(custom_key, message):
    key = len(custom_key)
    # create a list of length with empty strings
    cipher_text = [''] * key

    for col in range(key):
        currentIndex = col
        # traverse the message from index with step key
        while currentIndex < len(message):
            cipher_text[custom_key[col]] += message[currentIndex]
            currentIndex += key
    return ''.join(cipher_text)

# Run function main() when file.py is run
if __name__ == "__main__":
    main()
