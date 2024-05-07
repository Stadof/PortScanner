import socket
from tqdm import tqdm

# ANSI escape sequence for colour
RED = "\033[91m" # Red
GREEN = "\033[32m" # Green
RESET = "\033[0m" # Reset

def print_menu():
    print("=========================================")
    print("===========  Port Scanner Menu  =========")
    print("=========================================")
    print("1. Scan Custom Port Range")
    print("2. Scan Most Common Ports")
    print("3. Exit")
    print("=========================================")

print()
print("===============================================================")
print("========================  St4doF  =============================")
print("===============================================================")
print()

# Input IP
target = input("Enter the target IP address: ")
print()

while True:
    print_menu()
    print()
    choice = input("Enter your choice (1, 2, or 3): ")
    print()
    print()

    if choice == "1":
        # Accept a range of ports to scan
        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))
        ports = list(range(start_port, end_port + 1))
        break
    elif choice == "2":
        # Most common ports
        ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995]
        break
    elif choice == "3":
        print("Exiting.")
        exit()
    else:
        print(f"{RED}Invalid choice. Please enter 1, 2, or 3.{RED}")

for port in tqdm(ports, desc="Scanning ports"):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        service_name = socket.getservbyport(port)
        print()
        print(f" {GREEN}=> Port {port} ({service_name}) is open{RESET}")
    sock.close()

    # Wait for user input before exiting
print()
input(f"{RED}Scan complete. Press Enter to exit.{RED}")
