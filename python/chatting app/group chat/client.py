import socket
import threading

# Client configuration
HOST = '127.0.0.1'
PORT = 5555

# Function to receive messages from the server
def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            print(message)
        except:
            # Exit the thread if an exception occurs
            break

# Main client logic
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    name = input("Enter your name: ")
    client.send(bytes(name,'utf-8'))
    # Start a separate thread to receive messages
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    try:
        while True:
            message = input('\t\t\t\t')
            client.send(message.encode('utf-8'))
    except KeyboardInterrupt:
        print("You have left the chat.")
    finally:
        client.close()

# Start the client
start_client()
