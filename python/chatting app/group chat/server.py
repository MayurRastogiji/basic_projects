import socket
import threading


# Server configuration
HOST = '127.0.0.1'
PORT = 5555

# List to store connected clients
clients = []
client_names = []

# Function to broadcast messages to all connected clients
def broadcast(message, sender_name):
    for client, name in zip(clients, client_names):
        if name != sender_name:
            try:
                client.send(f"{sender_name}: {message}".encode('utf-8'))
            except:
                # Remove the client if unable to send message
                clients.remove(client)
                client_names.remove(name)
                broadcast_leave_message(name)
        else:
             client.send(f"you: {message}".encode('utf-8'))           
# Function to broadcast leave message when a client disconnects
def broadcast_leave_message(username):
    leave_message = f"{username} left the chat"
    for client in clients:
        try:
            client.send(leave_message.encode('utf-8'))
        except:
            # Remove the client if unable to send leave message
            clients.remove(client)

# Function to broadcast join message when a client connects
def broadcast_join_message(username):
    join_message = f"{username} joined the chat"
    for client, name in zip(clients, client_names):
        if name != username:
            try:
                client.send(join_message.encode('utf-8'))
            except:
                # Remove the client if unable to send join message
                clients.remove(client)
                client_names.remove(name)
                broadcast_leave_message(name)

# Function to handle a single client
def handle_client(client, username):
    # Broadcast join message when a client connects
    broadcast_join_message(username)
    
    try:
        while True:
            message = client.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"{username}: {message}")
            broadcast(message, username)
    except:
        # Remove the client if an exception occurs
        clients.remove(client)
        client_names.remove(username)
        broadcast_leave_message(username)

# Main server logic
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server is listening on {HOST}:{PORT}")

    while True:
        client, address = server.accept()
        username = client.recv(1024).decode("utf-8")
        print(f"{username} joined the chat from {address}")

        # Add the new client and username to the lists
        client_names.append(username)
        clients.append(client)

        # Create a new thread for each client
        client_thread = threading.Thread(target=handle_client, args=(client, username))
        client_thread.start()

# Start the server
start_server()


