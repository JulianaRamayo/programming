import numpy as np

# Define a list for all characters
characters = [chr(i) for i in range(32, 55292)] #all characters

# Create mappings between characters and their corresponding indices
letter_to_index = dict(zip(characters, range(len(characters))))
index_to_letter = dict(zip(range(len(characters)), characters))

def create_key():
	"""
	Creates a random encryption key for Hill Cipher.

	: return: 15x15 matrix representing the encryption key (15x15 numpy array)
	"""

	# Generate a 15x15 matrix with random integers between 0 and 100
	array = np.random.randint(low=0, high=100, size=(15, 15))
	return array

# Define encryption function using Hill cipher
def encryption(message, key):
	"""
	Encrypts a message using Hill Cipher.

	: message: The message to be encrypted (string)
	: key: The encryption key matrix (15x15 numpy array)
	: return: The encrypted message as a matrix (nx15 numpy array)
	"""

	encrypted = ''
	message_in_numbers = []
	
	# Convert characters in the message to their respective indices
	for letter in message:
		message_in_numbers.append(letter_to_index[letter])
	
	# Add zeros to the message to make its lenght a multiple of 15
	while len(message_in_numbers) % 15 != 0:
		message_in_numbers.append(0)

	# Reshape the message into a matrix and peform encryption using the provided key
	message_div = np.array(message_in_numbers).reshape(int(len(message_in_numbers) / 15), 15)
	message_encrypted = np.dot(message_div, key)

	return message_encrypted

# Define decryption function for Hill cipher
def decryption(message_encrypted, key):
	"""
	Decrypts an encrypted message using Hill Cipher.
	: message_encrypted: The encrypted message as a matrix (nx15 numpy array)
	: key: The encryption key matrix (15x15 numpy array)
	: return: Decrypted message (string)
	"""

	# Calculate the inverse of the key matrix
	matrix_inv = np.linalg.inv(key)

	# Decrypt the message multiplying the encrypted message with the inverse key
	multiplication = np.dot(message_encrypted, matrix_inv)
	multiplication = np.round_(multiplication).astype(int)

	# Flatten the decrypted message
	message_in_numbers = multiplication.flatten()
	
	# Convert indices back to characters
	decrypted = []
	for number in message_in_numbers:
		decrypted.append(index_to_letter[number])

	# Remove additional spaces from decrypted message
	while decrypted and decrypted[-1].isspace():
        	decrypted.pop()

	message_decrypted = ''.join(decrypted)
	return(message_decrypted)

''' FIRST EXAMPLE '''

# Generate a random encryption key
encryption_key = create_key()

# Message to be encrypted
original_message = "Hello, this is a secret message."

# Encryption
encrypted_message = encryption(original_message, encryption_key)

# Decryption
decrypted_message = decryption(encrypted_message, encryption_key)

# Print the results
print("Original Message: ", original_message)
print("Encrypted Message: ", encrypted_message)
print("Decrypted Message: ", decrypted_message)

'''SECOND EXAMPLE'''

# Define the encryption key matrix
key = create_key()

# Get message from the user
message = input('Enter message: ')

# Encrypt the message using the provided key
message_encrypted = encryption(message, key)

# Decrypt the encrypted message using the provided key
message_decrypted = decryption(message_encrypted, key)

# Print the results
print("Original Message: ", message)
print("Encrypted Message: ", message_encrypted)
print("Decrypted Message: ", message_decrypted)