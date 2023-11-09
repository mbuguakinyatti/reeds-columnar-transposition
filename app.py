from flask import Flask, render_template, request

from encryption import transposeEncrypt

app = Flask(__name__)
encryption_key = None  # Define a global variable for the encryption key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    global encryption_key  # Use the global variable for the encryption key
    message = request.form['message']
    encrypt_key = request.form.get('encrypt_key', '')  # Get the encryption key (if provided)

    # Use a default key if none is provided
    if not encrypt_key:
        encrypt_key = '012345678'

    # Check if the encryption key is too long
    encryption_key= encrypt_key
    length = len(encryption_key)
    print(encrypt_key)
    if length <=3 and length > 9:
        return "Encryption Key must not exceed 9 characters."

    encryption_key = [ord(char) for char in encrypt_key]  # Store the key in the global variable
    cipher_text = transposeEncrypt(encryption_key, message)
    return render_template('result.html', original_message=message, custom_key=encrypt_key, cipher_text=cipher_text)

if __name__ == '__main__':
    app.run(debug=True)
