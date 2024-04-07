# Imports modules needed to run script
# Used to choose random ASCII artwork
import random
# Used to exit program
import sys
# Used to run external commands
import subprocess
# Used to obtain system paths
import os

# Defines art display function
def art_dis():
    # List that defines numbers to be chosen at random
    rand_ascii = [1, 2, 3]
    # Chooses number at random from list
    rand_choi = random.choice(rand_ascii)

    # If statements that decide which ascii art will display when program starts
    if rand_choi == 1:
        print(r"     ___           ___                    ___           ___           ___           ___")
        print(r"    /\  \         |\__\                  /\  \         /\  \         /\  \         /\__\\")
        print(r"   /::\  \        |:|  |                /::\  \       /::\  \       /::\  \       /::|  |")
        print(r"  /:/\:\  \       |:|  |               /:/\ \  \     /:/\:\  \     /:/\:\  \     /:|:|  |")
        print(r" /::\~\:\  \      |:|__|__            _\:\~\ \  \   /:/  \:\  \   /::\~\:\  \   /:/|:|  |__")
        print(r"/:/\:\ \:\__\     /::::\__\          /\ \:\ \ \__\ /:/__/ \:\__\ /:/\:\ \:\__\ /:/ |:| /\__\\")
        print(r"\/__\:\/:/  /    /:/~~/~             \:\ \:\ \/__/ \:\  \  \/__/ \/__\:\/:/  / \/__|:|/:/  /")
        print(r"     \::/  /    /:/  /                \:\ \:\__\    \:\  \            \::/  /      |:/:/  /")
        print(r"      \/__/     \/__/                  \:\/:/  /     \:\  \           /:/  /       |::/  /")
        print(r"                                        \::/  /       \:\__\         /:/  /        /:/  /")
        print(r"                                         \/__/         \/__/         \/__/         \/__/")
    elif rand_choi == 2:
        print(r"     ___                              ___           ___           ___           ___")
        print(r"    /\  \                            /\__\         /\__\         /\  \         /\  \\")
        print(r"   /::\  \       ___                /:/ _/_       /:/  /        /::\  \        \:\  \\")
        print(r"  /:/\:\__\     /|  |              /:/ /\  \     /:/  /        /:/\:\  \        \:\  \\")
        print(r" /:/ /:/  /    |:|  |             /:/ /::\  \   /:/  /  ___   /:/ /::\  \   _____\:\  \\")
        print(r"/:/_/:/  /     |:|  |            /:/_/:/\:\__\ /:/__/  /\__\ /:/_/:/\:\__\ /::::::::\__\\")
        print(r"\:\/:/  /    __|:|__|            \:\/:/ /:/  / \:\  \ /:/  / \:\/:/  \/__/ \:\~~\~~\/__/")
        print(r" \::/__/    /::::\  \             \::/ /:/  /   \:\  /:/  /   \::/__/       \:\  \\")
        print(r"  \:\  \    ~~~~\:\  \             \/_/:/  /     \:\/:/  /     \:\  \        \:\  \\")
        print(r"   \:\__\        \:\__\              /:/  /       \::/  /       \:\__\        \:\__\\")
        print(r"    \/__/         \/__/              \/__/         \/__/         \/__/         \/__/")
    else:
        print(r"                                           ___           ___           ___           ___")
        print(r"      ___           __                    /  /\         /  /\         /  /\         /  /\\")
        print(r"     /  /\         |  |\                 /  /::\       /  /::\       /  /::\       /  /::|")
        print(r"    /  /::\        |  |:|               /__/:/\:\     /  /:/\:\     /  /:/\:\     /  /:|:|")
        print(r"   /  /:/\:\       |  |:|              _\_ \:\ \:\   /  /:/  \:\   /  /::\ \:\   /  /:/|:|__")
        print(r"  /  /::\ \:\      |__|:|__           /__/\ \:\ \:\ /__/:/ \  \:\ /__/:/\:\_\:\ /__/:/ |:| /\\")
        print(r" /__/:/\:\_\:\     /  /::::\          \  \:\ \:\_\/ \  \:\  \__\/ \__\/  \:\/:/ \__\/  |:|/:/")
        print(r" \__\/  \:\/:/    /  /:/~~~~           \  \:\_\:\    \  \:\            \__\::/      |  |:/:/")
        print(r"      \  \::/    /__/:/                 \  \:\/:/     \  \:\           /  /:/       |__|::/")
        print(r"       \__\/     \__\/                   \  \::/       \  \:\         /__/:/        /__/:/")
        print(r"                                          \__\/         \__\/         \__\/         \__\/")
        # Welcome statement
    print("Welcome to Py-Scan, a simple Python Nmap tool!")


# Defines scanner options function
def scan_opt():
    # Displays list of scan options
    print("1)TCP Scan\n"
          "2)UDP Scan\n"
          "3)Comprehensive Scan\n"
          "4)Ping\n"
          "5)Traceroute\n"
          "6)Show Options\n"
          "7)Exit")


# Defines port scanner function
def port_scan():
    # Prompts user for desired option
    scan_type = input("Please enter desired option here: ")
    # Series of statements chosen by user's previous input
    if scan_type == "1" or scan_type.lower() == "tcp" or scan_type.lower() == "tcp scan":
        # Prompts user for desired target
        scan_targ = input("Please enter desired target here: ")
        # Asks user if they would like results saved to a text file
        save_scan = input("Would you like the results saved to a text file: ")
        # Series of if statements regarding storing results in text file decided by user input
        if save_scan.lower() == "y" or save_scan.lower() == "yes":
            # Prompts user to enter file name for results to be saved to
            file_name = input("Please enter file name for the scan results: ")
            # Informs user of chosen scan type and target
            print("TCP scan has been chosen against the target: ", scan_targ)
            print("Please wait...")
            # The command being run with chosen option
            # This runs a TCP scan against the 1000 most common ports by default
            com = ["nmap", "-sS", scan_targ]
            # Stores result within variable
            com_res = subprocess.run(com, capture_output=True, text=True)
            # Prints result in standard output
            print(com_res.stdout)
            # Retrieve user's desktop directory
            desk_dir = os.path.expanduser("~/OneDrive/Desktop/")
            # Append chosen file name to path
            file_app = os.path.join(desk_dir, file_name)
            # Creates and writes to text file to store nmap results
            res_file = open(file_app, "a")
            res_file.write("TCP Scan Results:\n ")
            # Appends results to and closes text file
            res_file.write(com_res.stdout)
            res_file.write("-----\n")
            res_file.close()
            print("Restarting...")
            port_scan()
        elif save_scan.lower() == "n" or save_scan.lower() == "no":
            # Informs user of chosen scan type and target
            print("TCP scan has been chosen against the target: ", scan_targ)
            print("Please wait...")
            # The command being run with chosen option
            # This runs a TCP scan against the 1000 most common ports by default
            com = ["nmap", "-sS", scan_targ]
            # Stores result within variable
            com_res = subprocess.run(com, capture_output=True, text=True)
            # Prints result in standard output
            print(com_res.stdout)
            # Restarts port scan function
            print("Restarting...")
            port_scan()
        else:
            # Informs user of invalid option
            print("User input for saving scan to text file was not properly defined...")
            print("Running scan anyway...")
            # Informs user of chosen scan type and target
            print("TCP scan has been chosen against the target: ", scan_targ)
            print("Please wait...")
            # The command being run with chosen option
            # This runs a TCP scan against the 1000 most common ports by default
            com = ["nmap", "-sS", scan_targ]
            # Stores result within variable
            com_res = subprocess.run(com, capture_output=True, text=True)
            # Prints result in standard output
            print(com_res.stdout)
            # Restarts port scan function
            print("Restarting...")
            port_scan()

    elif scan_type == "2" or scan_type.lower() == "udp" or scan_type.lower() == "udp scan":
        # Prompts user for desired target
        scan_targ = input("Please enter desired target here: ")
        # Asks user if they would like results saved to a text file
        save_scan = input("Would you like the results saved to a text file: ")
        # Series of if statements regarding storing results in text file decided by user input
        if save_scan.lower() == "y" or save_scan.lower() == "yes":
            # Prompts user to enter file name for results to be saved to
            file_name = input("Please enter file name for the scan results: ")
            # Informs user of chosen scan type and target
            print("UDP scan has been chosen against the target: ", scan_targ)
            print("Please wait...")
            # The command being run with chosen option
            # This runs a UDP scan against the 1000 most common ports by default
            com = ["nmap", "-sU", scan_targ]
            # Stores result within variable
            com_res = subprocess.run(com, capture_output=True, text=True)
            # Prints result in standard output
            print(com_res.stdout)
            # Retrieve user's desktop directory
            desk_dir = os.path.expanduser("~/OneDrive/Desktop/")
            # Append chosen file name to path
            file_app = os.path.join(desk_dir, file_name)
            # Creates and writes to text file to store nmap results
            res_file = open(file_app, "a")
            res_file.write("UDP Scan Results:\n ")
            # Appends results to and closes text file
            res_file.write(com_res.stdout)
            res_file.write("-----\n")
            res_file.close()
            print("Restarting...")
            port_scan()
        elif save_scan.lower() == "n" or save_scan.lower() == "no":
            # Informs user of chosen scan type and target
            print("UDP scan has been chosen against the target: ", scan_targ)
            print("Please wait...")
            # The command being run with chosen option
            # This runs a UDP scan against the 1000 most common ports by default
            com = ["nmap", "-sU", scan_targ]
            # Stores result within variable
            com_res = subprocess.run(com, capture_output=True, text=True)
            # Prints result in standard output
            print(com_res.stdout)
            # Restarts port scan function
            print("Restarting...")
            port_scan()
        else:
            # Informs user of invalid option
            print("User input for saving scan to text file was not properly defined...")
            print("Running scan anyway...")
            # Informs user of chosen scan type and target
            print("UDP scan has been chosen against the target: ", scan_targ)
            print("Please wait...")
            # The command being run with chosen option
            # This runs a UDP scan against the 1000 most common ports by default
            com = ["nmap", "-sU", scan_targ]
            # Stores result within variable
            com_res = subprocess.run(com, capture_output=True, text=True)
            # Prints result in standard output
            print(com_res.stdout)
            # Restarts port scan function
            print("Restarting...")
            port_scan()

    elif scan_type == "3" or scan_type.lower() == "comprehensive scan" or scan_type.lower() == "comp":
        # Prompts user for desired target
        scan_targ = input("Please enter desired target here: ")
        # Asks user if they would like results saved to a text file
        save_scan = input("Would you like the results saved to a text file: ")
        # Series of if statements regarding storing results in text file decided by user input
        if save_scan.lower() == "y" or save_scan.lower() == "yes":
            # Prompts user to enter file name for results to be saved to
            file_name = input("Please enter file name for the scan results: ")
            # Informs user of chosen scan type and target
            print("Comprehensive scan has been chosen against the target: ", scan_targ)
            print("Please wait...")
            # The command being run with chosen option
            # This runs a comprehensive scan against with version detection
            com = ["nmap", "-sSUV", scan_targ]
            # Stores result within variable
            com_res = subprocess.run(com, capture_output=True, text=True)
            # Prints result in standard output
            print(com_res.stdout)
            # Retrieve user's desktop directory
            desk_dir = os.path.expanduser("~/OneDrive/Desktop/")
            # Append chosen file name to path
            file_app = os.path.join(desk_dir, file_name)
            # Creates and writes to text file to store nmap results
            res_file = open(file_app, "a")
            res_file.write("Comprehensive Scan Results:\n ")
            # Appends results to and closes text file
            res_file.write(com_res.stdout)
            res_file.write("-----\n")
            res_file.close()
            print("Restarting...")
            port_scan()
        elif save_scan.lower() == "n" or save_scan.lower() == "no":
            # Informs user of chosen scan type and target
            print("Comprehensive scan has been chosen against the target: ", scan_targ)
            print("Please wait...")
            # The command being run with chosen option
            # This runs a comprehensive scan against with version detection
            com = ["nmap", "-sSUV", scan_targ]
            # Stores result within variable
            com_res = subprocess.run(com, capture_output=True, text=True)
            # Prints result in standard output
            print(com_res.stdout)
            # Restarts port scan function
            print("Restarting...")
            port_scan()
        else:
            # Informs user of invalid option
            print("User input for saving scan to text file was not properly defined...")
            print("Running scan anyway...")
            # Informs user of chosen scan type and target
            print("Comprehensive scan has been chosen against the target: ", scan_targ)
            print("Please wait...")
            # The command being run with chosen option
            # This runs a comprehensive scan against with version detection
            com = ["nmap", "-sSUV", scan_targ]
            # Stores result within variable
            com_res = subprocess.run(com, capture_output=True, text=True)
            # Prints result in standard output
            print(com_res.stdout)
            # Restarts port scan function
            print("Restarting...")
            port_scan()

    elif scan_type == "4" or scan_type.lower() == "ping" or scan_type.lower() == "ping scan":
        # Prompts user for desired target
        scan_targ = input("Please enter desired target here: ")
        # Asks user if they would like results saved to a text file
        save_scan = input("Would you like the results saved to a text file: ")
        # Series of if statements regarding storing results in text file decided by user input
        if save_scan.lower() == "y" or save_scan.lower() == "yes":
            # Prompts user to enter file name for results to be saved to
            file_name = input("Please enter file name for the scan results: ")
            # Informs user of chosen scan type and target
            print("Ping scan has been chosen against the target: ", scan_targ)
            print("Please wait...")
            # The command being run with chosen option
            # This runs a ping scan against the target
            com = ["nmap", "-sn", scan_targ]
            # Stores result within variable
            com_res = subprocess.run(com, capture_output=True, text=True)
            # Prints result in standard output
            print(com_res.stdout)
            # Retrieve user's desktop directory
            desk_dir = os.path.expanduser("~/OneDrive/Desktop/")
            # Append chosen file name to path
            file_app = os.path.join(desk_dir, file_name)
            # Creates and writes to text file to store nmap results
            res_file = open(file_app, "a")
            res_file.write("Ping Scan Results:\n ")
            # Appends results to and closes text file
            res_file.write(com_res.stdout)
            res_file.write("-----\n")
            res_file.close()
            print("Restarting...")
            port_scan()
        elif save_scan.lower() == "n" or save_scan.lower() == "no":
            # Informs user of chosen scan type and target
            print("Ping scan has been chosen against the target: ", scan_targ)
            print("Please wait...")
            # The command being run with chosen option
            # This runs a ping scan against the target
            com = ["nmap", "-sn", scan_targ]
            # Stores result within variable
            com_res = subprocess.run(com, capture_output=True, text=True)
            # Prints result in standard output
            print(com_res.stdout)
            # Restarts port scan function
            print("Restarting...")
            port_scan()
        else:
            # Informs user of invalid option
            print("User input for saving scan to text file was not properly defined...")
            print("Running scan anyway...")
            # Informs user of chosen scan type and target
            print("Ping scan has been chosen against the target: ", scan_targ)
            print("Please wait...")
            # The command being run with chosen option
            # This runs a ping scan against the target
            com = ["nmap", "-sn", scan_targ]
            # Stores result within variable
            com_res = subprocess.run(com, capture_output=True, text=True)
            # Prints result in standard output
            print(com_res.stdout)
            # Restarts port scan function
            print("Restarting...")
            port_scan()

    elif scan_type == "5" or scan_type.lower() == "traceroute" or scan_type.lower() == "trace":
        # Prompts user for desired target
        scan_targ = input("Please enter desired target here: ")
        # Asks user if they would like results saved to a text file
        save_scan = input("Would you like the results saved to a text file: ")
        # Series of if statements regarding storing results in text file decided by user input
        if save_scan.lower() == "y" or save_scan.lower() == "yes":
            # Prompts user to enter file name for results to be saved to
            file_name = input("Please enter file name for the scan results: ")
            # Informs user of chosen scan type and target
            print("Traceroute scan has been chosen against the target: ", scan_targ)
            print("Please wait...")
            # The command being run with chosen option
            # This runs a Traceroute scan against the target
            com = ["nmap", "-sn", "--traceroute", scan_targ]
            # Stores result within variable
            com_res = subprocess.run(com, capture_output=True, text=True)
            # Prints result in standard output
            print(com_res.stdout)
            # Retrieve user's desktop directory
            desk_dir = os.path.expanduser("~/OneDrive/Desktop/")
            # Append chosen file name to path
            file_app = os.path.join(desk_dir, file_name)
            # Creates and writes to text file to store nmap results
            res_file = open(file_app, "a")
            res_file.write("Traceroute Scan Results:\n ")
            # Appends results to and closes text file
            res_file.write(com_res.stdout)
            res_file.write("-----\n")
            res_file.close()
            print("Restarting...")
            port_scan()
        elif save_scan.lower() == "n" or save_scan.lower() == "no":
            # Informs user of chosen scan type and target
            print("Traceroute scan has been chosen against the target: ", scan_targ)
            print("Please wait...")
            # The command being run with chosen option
            # This runs a Traceroute scan against the target
            com = ["nmap", "-sn", "--traceroute", scan_targ]
            # Stores result within variable
            com_res = subprocess.run(com, capture_output=True, text=True)
            # Prints result in standard output
            print(com_res.stdout)
            # Restarts port scan function
            print("Restarting...")
            port_scan()
        else:
            # Informs user of invalid option
            print("User input for saving scan to text file was not properly defined...")
            print("Running scan anyway...")
            # Informs user of chosen scan type and target
            print("Traceroute scan has been chosen against the target: ", scan_targ)
            print("Please wait...")
            # The command being run with chosen option
            # This runs a Traceroute scan against the target
            com = ["nmap", "-sn", "--traceroute", scan_targ]
            # Stores result within variable
            com_res = subprocess.run(com, capture_output=True, text=True)
            # Prints result in standard output
            print(com_res.stdout)
            # Restarts port scan function
            print("Restarting...")
            port_scan()

    elif scan_type == "6" or scan_type.lower() == "option" or scan_type.lower() == "options":
        # Runs scan option function
        scan_opt()
        # Restarts port scan function
        port_scan()

    elif scan_type == "7" or scan_type.lower() == "e" or scan_type.lower() == "exit":
        # Informs user of exit
        print("Thank you for using Py-Scan!")
        print("Exiting...")
        # Exits program
        sys.exit()

    else:
        # Occurs when invalid option is chosen
        print("Invalid Option!")
        print("Restarting...")
        # Restarts program
        port_scan()


# Runs the art display function
art_dis()
# Runs the scan options function
scan_opt()
# Runs the scanner function
port_scan()
