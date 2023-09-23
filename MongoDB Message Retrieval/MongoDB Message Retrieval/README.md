# Project Messaging System Readme
Project Messaging System Readme
This README provides an overview of a Python script for a simple messaging system that utilizes MongoDB as the backend database. It includes instructions for setup and usage.

## Prerequisites
Before running the code, ensure that you have the following prerequisites installed:

-Python 3.x
-The pymongo library
-Access to a MongoDB instance

## Getting Started
1. Clone or download the project to your local machine.
2. Install the required Python packages by running the following command in your terminal:

```bash
pip install pymongo
```
3. Replace the 'uri' variable in the code with your MongoDB connection string. You can obtain this connection string from your MongoDB instance.

## Running the Application
To run the messaging system, follow these steps:

1. Open a terminal and navigate to the project directory.
2. Run the following command to start the application:
```bash
python script.py
```
3.You will be presented with two options:
    -To send a message, type 's' and press Enter. You will be prompted to enter your message.
    -To exit the application, type 'e' and press Enter.

4. The application also has a background thread that continuously checks for and displays the last received message. Messages will be displayed in the format: username: message.

5. You can send and receive messages as long as the application is running. To exit, simply type 'e' and press Enter.

## Customization
You can customize the application by adjusting the sleep interval in the receive_and_display_last_message function. By default, it checks for new messages every 2 seconds. You can change this interval to suit your preferences.

## Dependencies
- `python3`: For running the code.
- `pymongo`: For interacting with the MongoDB database.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)