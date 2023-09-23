# Hill Cipher Encryption and Decryption

This folder contains Python code to perform encryption and decryption using the Hill Cipher, a classic symmetric encryption algorithm. The code demonstrates the encryption and decryption processes.

## Code Overview

### Key Generation
The function `create_key()` generates a random 15x15 encryption key matrix for the Hill Cipher.

### Encryption
The `encryption(message, key)` function encrypts a given message using the Hill Cipher. It converts characters in the message to their respective indices, reshapes the message into a matrix, and performs encryption using the provided key.

### Decryption
The `decryption(message_encrypted, key)` function decrypts an encrypted message using the Hill Cipher. It calculates the inverse of the key matrix, multiplies the encrypted message with the inverse key, and converts indices back to characters to obtain the decrypted message.

## Running the Code

Two examples demonstrate the encryption and decryption processes using the generated encryption key.

### First Example
1. A random encryption key is generated.
2. An original message is defined.
3. The original message is encrypted using the generated encryption key.
4. The encrypted message is decrypted using the same encryption key.
5. Original message, encrypted message, and decrypted message are printed.

### Second Example
1. A random encryption key is generated.
2. The user is prompted to enter a message.
3. The entered message is encrypted using the generated encryption key.
4. The encrypted message is decrypted using the same encryption key.
5. Entered message, encrypted message, and decrypted message are printed.

## Importance of Invertible Key Matrix

In encryption, an invertible key matrix is crucial for successful decryption. If the key matrix is not invertible, decryption becomes impossible, rendering the encrypted message irretrievable. An invertible key matrix ensures that decryption can accurately reconstruct the original message from the encrypted form.

Feel free to explore the provided code and experiment with different messages and encryption keys to observe the encryption and decryption processes.