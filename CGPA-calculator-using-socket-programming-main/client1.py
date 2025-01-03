
import socket
import tkinter as tk
from tkinter import messagebox

# Function to communicate with the server and get CGPA
def send_grades():
    try:
        # Get the marks from the input fields
        marks = [float(entry.get()) for entry in entries]

        # Create a TCP/IP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the server
        client_socket.connect(('127.0.0.1', 65432))

        # Send the marks to the server
        marks_str = ','.join(map(str, marks))
        client_socket.sendall(marks_str.encode())

        # Receive the CGPA from the server
        cgpa = client_socket.recv(1024).decode()

        # Update the result label with the CGPA
        result_label.config(text=f"Your CGPA is: {cgpa}")

        # Close the socket
        client_socket.close()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to dynamically generate input fields for the subjects
def create_subject_fields():
    global entries
    entries = []

    try:
        # Get the number of subjects
        num_subjects = int(num_subjects_entry.get())

        # Remove existing entries if any
        for widget in entry_frame.winfo_children():
            widget.destroy()

        # Create labels and entry fields for each subject
        for i in range(num_subjects):
            label = tk.Label(entry_frame, text=f"Subject {i + 1} Marks (out of 100):", font=("Arial", 14), bg="#f2f2f2")
            label.grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(entry_frame, font=("Arial", 14), width=10, justify='center')
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries.append(entry)

        # Create a submit button (placed at the bottom after the subjects)
        submit_button = tk.Button(entry_frame, text="Calculate CGPA", command=send_grades, font=("Arial", 14), bg="#4CAF50", fg="white", width=20)
        submit_button.grid(row=num_subjects, column=1, padx=10, pady=20)

        # Update the result label to clear previous results
        result_label.config(text="")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of subjects")

# Function to create the main GUI
def create_gui():
    global num_subjects_entry, entry_frame, result_label

    # Create the main window
    root = tk.Tk()
    root.title("CGPA Calculator")

    # Set the size of the window
    root.geometry("600x400")
    root.configure(bg="#f2f2f2")

    # Input for the number of subjects
    label = tk.Label(root, text="Enter Number of Subjects:", font=("Arial", 16), bg="#f2f2f2")
    label.grid(row=0, column=0, padx=10, pady=20)
    num_subjects_entry = tk.Entry(root, font=("Arial", 16), width=5)
    num_subjects_entry.grid(row=0, column=1, padx=10, pady=20)

    # Button to generate subject input fields
    generate_button = tk.Button(root, text="Generate Subject Fields", command=create_subject_fields, font=("Arial", 16), bg="#2196F3", fg="white")
    generate_button.grid(row=0, column=2, padx=10, pady=20)

    # Frame to hold the dynamically generated subject fields
    entry_frame = tk.Frame(root, bg="#f2f2f2")
    entry_frame.grid(row=1, column=0, columnspan=3)

    # Frame for displaying the result
    result_frame = tk.Frame(root, bg="#e0f7fa", borderwidth=2, relief="groove")
    result_frame.grid(row=2, column=0, columnspan=3, padx=20, pady=20)
    
    # Result label
    result_label = tk.Label(result_frame, text="", font=("Arial", 20, "bold"), bg="#e0f7fa", fg="#00796b")
    result_label.pack(padx=20, pady=20)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()
