def transposeEncrypt(custom_key, message):
    key_length = len(custom_key)
    message_length = len(message)
    cipher_text = [''] * key_length

    for col in range(key_length):
        currentIndex = col
        while currentIndex < message_length:
            cipher_text[custom_key[col]% key_length] += message[currentIndex]
            currentIndex += key_length


    myString = ''  
    for i in cipher_text:
        myString += ' ' + i
    return myString
