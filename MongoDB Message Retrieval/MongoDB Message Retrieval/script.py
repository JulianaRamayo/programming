# Import necessary libraries
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import time
import threading
from pymongo import DESCENDING

# MongoDB connection configuration
uri = " " # Replace this with your MongoDB URI
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["Project"]
collection = db["messages"]

# Function to send messages
def send_msg(message):
    msg = message
    # Extract the username from the MongoDB URI
    username = uri.replace('mongodb+srv://', '')
    caracter = ":"

    # Find the position of the ':' character in the username
    pos = username.find(caracter)
    if pos != -1:
        username = username[:pos]

    # Create a message data dictionary
    msg_data= {
        'username': username ,
        'message' : msg,
        'time': time.time()
    }
    
    # Insert the message data into the MongoDB collection
    collection.insert_one(msg_data)

# Function to receive and display the last message
def receive_and_display_last_message():
    last_message = None
    while True:
        # Retrieve the current last message from the collection, sorted by time
        current_last_message = collection.find_one(sort=[('time', DESCENDING)])
        
        # Check if a new message is received and it's different from the last one
        if current_last_message and current_last_message != last_message:
            username = current_last_message['username']
            msg = current_last_message['message']
            timestamp = current_last_message['time']

            # Format the last sent message for display
            formatted_message = f"{username}: {msg}"

            # Print the formatted message
            print(formatted_message)

            # Update the last message
            last_message = current_last_message
        
        # Adjust the sleep interval as needed (2 seconds by default)
        time.sleep(2)  # Adjust the sleep interval as needed

# Main function
def main():
    # Create a thread for receiving and displaying the last message
    receive_thread = threading.Thread(target=receive_and_display_last_message)
    receive_thread.daemon = True
    receive_thread.start()

    while True:
        sending = input("Do you want to send a message (s) or exit (e)? (s/e): ")
        if sending == "s":
            msg = input("Enter your message: ")
            send_msg(msg)
        elif sending == "e":
            break
        else:
            print("Invalid option. Please enter 's' or 'e'.")

if __name__ == "__main__":
    main()