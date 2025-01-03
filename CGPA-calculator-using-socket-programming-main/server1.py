import socket

# Function to calculate CGPA based on average marks
def calculate_cgpa(average_marks):
    return round(average_marks / 10.0, 2)

# Server setup
def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the loopback address and port
    server_socket.bind(('127.0.0.1', 65432))
    # Listen for incoming connections
    server_socket.listen(1)
    print("Server is listening on port 65432...")

    while True:
        # Wait for a connection
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        try:
            # Receive the data from the client
            data = conn.recv(1024)
            if not data:
                break

            # Decode the received data (marks from client)
            marks = list(map(float, data.decode().split(',')))

            # Calculate average marks
            average_marks = sum(marks) / len(marks)

            # Calculate CGPA based on the average marks
            cgpa = calculate_cgpa(average_marks)
            print(f"Received marks: {marks}, Average Marks: {average_marks}, Calculated CGPA: {cgpa}")

            # Send the CGPA back to the client
            conn.sendall(str(cgpa).encode())

        finally:
            # Clean up the connection
            conn.close()

if __name__ == "__main__":
    start_server()
