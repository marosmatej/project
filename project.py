import serial
import time

# Define COM port for communication
bluetooth_port = "/dev/tty.HC-06"


# Establish serial communication
try:
    bluetooth = serial.Serial(bluetooth_port, 9600, timeout=1)
    print("Bluetooth connection established on port " + bluetooth_port)
except serial.SerialException:
    print("Failed to connect. Chcek the COM port. ")
    exit()

def send_command(command):
    bluetooth.write(command.encode())
    time.sleep(0.1)

while True:
    user_input = input("Enter command (F/B/L/R): ")
    
    if user_input.upper() == 'F':
        send_command('F')  # Forward
    elif user_input.upper() == 'B':
        send_command('B')  # Backward
    elif user_input.upper() == 'L':
        send_command('L')  # Left
    elif user_input.upper() == 'R':
        send_command('R')  # Right
    else:
        print("Invalid command. Please enter F/B/L/R.")

# Close serial connection
bluetooth.close()
